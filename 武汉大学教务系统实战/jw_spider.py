#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: Gary
#versions :1.8.4 教务系统更新2019.12.29
#登录带上了时间戳，jwb,检测浏览器，url更换，请求不能过快等,验证码函数单独出来

from io import BytesIO#打开图片
import requests#处理post、get等请求
from  PIL import Image#处理图片
import hashlib#密码加密
import datetime,time#处理时间戳
from bs4 import BeautifulSoup as bs#解析网页
from lxml import etree

#教务系统采用的MD5加密
def md5value(password):
    password=password.encode()
    md5 = hashlib.md5()
    md5.update(password)
    return md5.hexdigest()

#获取csrftoken，后面很多地方都用的到
def csrf(str):
    soup = bs(str,'html.parser')
    c = {}
    for r in soup.find_all('div'):
        if r.get('onclick') != None:
            c[r.get('name')] = r.get('onclick')
    return c

#验证码函数
def code(s):
    header = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
    try:
        # 当前为手动输入验证码
        # imgUrl = 'http://bkjw.whu.edu.cn/servlet/GenImg'#验证码的url
        # imgUrl ="http://bkjw.whu.edu.cn/servlet/_CCFD344A"#新的验证码地址2019/12/25
        imgUrl = "http://bkjw.whu.edu.cn/servlet/_89ab36cec99d8d?v=2"  # 新的验证码地址2019/12/27，可以自己观察教务系更新
        #http://bkjw.whu.edu.cn/servlet/a2a0311db?v=2
        img = s.get(imgUrl, headers=header, stream=True)
        im = Image.open(BytesIO(img.content))
        im.show()
        code = input('请输入验证码:')
        return code,img.cookies
    except:
        print('验证码地址失效，请更新！')
        return -1,-1

#登录函数
def LoginByPost(username,password):
    header = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
    while True:
        s = requests.session()  # 获取一个会话,方便身份识别
        try:
            xdvfb,img_cookies=code(s)
            if xdvfb==-1:
                break
            #登录的相关操作
            #loginUrl = 'http://bkjw.whu.edu.cn/servlet/Login'#登录的url
            #loginUrl = "http://bkjw.whu.edu.cn/servlet/_8406BEE1" #分年级后的登录url2019/12/25
            #loginUrl="http://bkjw.whu.edu.cn/servlet/_7052447"#登录url更新2019/12/27
            loginUrl='http://bkjw.whu.edu.cn/servlet/b89d79056'#2019/12/29更新，可以自己观察教务系统更新
            #print(md5value(password))
            current_milli_time = lambda: int(round(time.time() * 1000))#获取13位时间戳，原本python只有10，需要进行转换
            postData = {'timestamp':current_milli_time(),'jwb':'%E6%AD%A6%E5%A4%A7%E6%9C%AC%E7%A7%91%E6%95%99%E5%8A%A1%E7%B3%BB%E7%BB%9F','id': username, 'pwd': md5value(password), 'xdvfb': xdvfb}#登录需要post的数据,12/29请求添加了时间戳,和jwb
            rs = s.post(loginUrl, postData,headers=header, cookies=requests.utils.dict_from_cookiejar(img_cookies))  # 验证码带cookie
            rs.encoding = rs.apparent_encoding
            #print(rs.text)
            LoginCookies = rs.cookies  # 登录后的cookie
            #print(LoginCookies.items)

            #获取csrftoken，获取成功即登录成功
            url = 'http://bkjw.whu.edu.cn/stu/stu_index.jsp'  # 获取csrftoken，很多操作都需要
            res = s.get(url, headers=header,cookies=requests.utils.dict_from_cookiejar(LoginCookies))  # 登录后带cookie
            res.encoding = res.apparent_encoding
            # print(res.text)
            ct = csrf(res.text)  # 获取csrftoken，后面选课用到
            csrftoken = ct[None].split("'")[1].split('csrftoken=')[-1]
            print("登录成功！")
            #print('csrftoken:', csrftoken)
            return s,LoginCookies,csrftoken
        except:
            #print(rs.text)#alertp
            s = etree.HTML(rs.text)
            alertp = s.xpath('//*[@id="loginInputBox"]/tr[4]/td/font/text()')#获取登录失败的原因，
            time.sleep(1)
            print(alertp[0])
            time.sleep(1)#防止过快被限制
            #print('登录失败请重试')


#获取所有公选课
def select_pub(s,cookie):
    header = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
    for page in range(1,23):
        print('第{}页'.format(page))
        url='http://bkjw.whu.edu.cn/stu/choose_PubLsn_list.jsp?XiaoQu=0&credit=0&keyword=&pageNum={}'.format(page)#课程链接
        #http://bkjw.whu.edu.cn/stu/choose_PubLsn_list.jsp?XiaoQu=0&credit=0&keyword=&pageNum=2
        res=s.get(url,headers=header,cookies=requests.utils.dict_from_cookiejar(cookie))
        res.encoding = res.apparent_encoding
        #print(res.text)
        data= etree.HTML(res.text)
        for i in range(2,17):
            Cid=int(data.xpath('/html/body/table/tr[{}]/td[13]/input/@lessonheadid'.format(i))[0])#lessonheadid,课头号
            Cname=data.xpath('/html/body/table/tr[{}]/td[1]/text()'.format(i))[0]#课程名
            Cgrade=data.xpath('/html/body/table/tr[{}]/td[2]/text()'.format(i))[0]#学分
            Csurplus = int(data.xpath('/html/body/table/tr[{}]/td[3]/font/text()'.format(i))[0])#课程剩余人数
            Cnum=data.xpath('/html/body/table/tr[{}]/td[3]/text()'.format(i))[0]#课程总人数
            Tname=data.xpath('/html/body/table/tr[{}]/td[4]/text()'.format(i))[0]#教师名
            Ttitle=data.xpath('/html/body/table/tr[{}]/td[5]/text()'.format(i))[0]#职称
            Tpart=data.xpath('/html/body/table/tr[{}]/td[6]/text()'.format(i))[0]#授课学院
            try:
                Tdomain=data.xpath('/html/body/table/tr[{}]/td[7]/text()'.format(i))[0]#领域
            except:
                Tdomain ='无'
            Tyear=int(data.xpath('/html/body/table/tr[{}]/td[8]/text()'.format(i))[0])#学年
            Tterm=int(data.xpath('/html/body/table/tr[{}]/td[9]/text()'.format(i))[0])#学期
            Tsite=str(data.xpath('normalize-space(/html/body/table/tr[{}]/td[10]/div[1]/text())'.format(i)))#上课时间地点
            Ttips=str(data.xpath('normalize-space(/html/body/table/tr[{}]/td[11]/div/text())'.format(i)))#备注
            print('第{}条'.format(i-1))
            print(Cid, Cname, Cgrade, Csurplus, Cnum, Tname, Ttitle, Tpart, Tdomain, Tyear, Tterm, Tsite, Ttips)
        
        time.sleep(2)  # 翻页过快会被限制
#soup不咋会，有兴趣的话可以自己尝试一下
    #soup = bs(res.text,"html.parser")
    #tables = soup.findAll('table')
    #tab = tables[0]
    #for tr in tab.tbody.findAll('tr'):
    #    for td in tr.findAll('td'):
    #        text =td.getText().encode('gb2312')
    #        print(text)
if __name__ == '__main__':
    username = username#账号
    password = 'password'#密码，得是字符
    s,cookie,csrftoken=LoginByPost(username, password)
    select_pub(s,cookie)
