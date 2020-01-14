# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Gary

from io import BytesIO  # 打开图片
import requests  # 处理post、get等请求
from PIL import Image  # 处理图片
import hashlib  # 密码加密
import datetime, time  # 处理时间戳
from bs4 import BeautifulSoup as bs  # 解析网页
from lxml import etree

week={0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}#周一到周日对应datetime的weekday数，0表示周一
month={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sept',10:'Oct',11:'Nov',12:'Dec'}#月份对照
# 教务系统采用的MD5加密
def md5value(password):
    password = password.encode()
    md5 = hashlib.md5()
    md5.update(password)
    return md5.hexdigest()


# 获取csrftoken，后面选课用到
def csrf(str):
    soup = bs(str, 'html.parser')
    c = {}
    for r in soup.find_all('div'):
        if r.get('onclick') != None:
            c[r.get('name')] = r.get('onclick')
    return c


# 验证码函数
def code(s):
    header = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
    try:
        # 当前为手动输入验证码
        # imgUrl = 'http://bkjw.whu.edu.cn/servlet/GenImg'#验证码的url
        # imgUrl ="http://bkjw.whu.edu.cn/servlet/_CCFD344A"#新的验证码地址2019/12/25
        imgUrl = "http://bkjw.whu.edu.cn/servlet/_89ab36cec99d8d?v=2"  # 新的验证码地址2019/12/27，可以自己观察教务系更新
        # http://bkjw.whu.edu.cn/servlet/a2a0311db?v=2
        img = s.get(imgUrl, headers=header, stream=True)
        im = Image.open(BytesIO(img.content))
        im.show()
        code = input('请输入验证码:')
        return code, img.cookies
    except:
        print('验证码地址失效，请更新！')
        return -1, -1


# 登录函数
def LoginByPost(username, password):
    header = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
    while True:
        s = requests.session()  # 获取一个会话,方便身份识别
        try:
            xdvfb, img_cookies = code(s)
            if xdvfb == -1:
                break
            # 登录的相关操作
            # loginUrl = 'http://bkjw.whu.edu.cn/servlet/Login'#登录的url
            # loginUrl = "http://bkjw.whu.edu.cn/servlet/_8406BEE1" #分年级后的登录url2019/12/25
            # loginUrl="http://bkjw.whu.edu.cn/servlet/_7052447"#登录url更新2019/12/27
            loginUrl = 'http://bkjw.whu.edu.cn/servlet/b89d79056'  # 2019/12/29更新，可以自己观察教务系统更新
            # print(md5value(password))
            current_milli_time = lambda: int(round(time.time() * 1000))  # 获取13位时间戳，原本python只有10，需要进行转换
            postData = {'timestamp': current_milli_time(),
                        'jwb': '%E6%AD%A6%E5%A4%A7%E6%9C%AC%E7%A7%91%E6%95%99%E5%8A%A1%E7%B3%BB%E7%BB%9F',
                        'id': username, 'pwd': md5value(password), 'xdvfb': xdvfb}  # 登录需要post的数据,12/29请求添加了时间戳,和jwb
            rs = s.post(loginUrl, postData, headers=header,
                        cookies=requests.utils.dict_from_cookiejar(img_cookies))  # 验证码带cookie
            rs.encoding = rs.apparent_encoding
            # print(rs.text)
            LoginCookies = rs.cookies  # 登录后的cookie
            # print(LoginCookies.items)

            # 获取csrftoken，获取成功即登录成功
            url = 'http://bkjw.whu.edu.cn/stu/stu_index.jsp'  # 获取csrftoken，很多操作都需要
            res = s.get(url, headers=header, cookies=requests.utils.dict_from_cookiejar(LoginCookies))  # 登录后带cookie
            res.encoding = res.apparent_encoding
            # print(res.text)
            ct = csrf(res.text)  # 获取csrftoken，后面很多地方都用的到
            csrftoken = ct[None].split("'")[1].split('csrftoken=')[-1]
            print("登录成功！")
            # print('csrftoken:', csrftoken)
            return s, LoginCookies, csrftoken
        except:
            # print(rs.text)#alertp
            s = etree.HTML(rs.text)
            alertp = s.xpath('//*[@id="loginInputBox"]/tr[4]/td/font/text()')  # 获取登录失败的原因，
            time.sleep(1)
            print(alertp[0])
            time.sleep(1)  # 防止过快被限制
            # print('登录失败请重试')


def ALL_GPA(s,cookies,csrftoken):
    header = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
    datetime_now=datetime.datetime.now()#获取当前的时间
    weekday=week[datetime_now.weekday()]#获取对应的周几英语缩写
    month_=month[datetime_now.month]#获取对应的几月份英语缩写
    day=datetime_now.day#获取日期
    year=datetime_now.year#获取年份
    time=datetime_now.strftime('%H:%M:%S')#格式化时间
    grade_url = 'http://bkjw.whu.edu.cn/servlet/Svlt_QueryStuScore?csrftoken={}&year=0&term=&learnType=&scoreFlag=0&t={}%20{}%20{}%20{}%20{}%20GMT+0800%20(%D6%D0%B9%FA%B1%EA%D7%BC%CA%B1%BC%E4)'.format(csrftoken,weekday,month_,day,year,time)#成绩的url
    #Mon%20Jan%2013%202020%2020:38:05%20GMT+0800%20(%D6%D0%B9%FA%B1%EA%D7%BC%CA%B1%BC%E4) 是指中国标准时间
    #Mon Jan 13 2020 20:38:05 GMT 0800 (中国标准时间)
    #print(grade_url)
    res = s.get(grade_url, headers=header, cookies=requests.utils.dict_from_cookiejar(cookies))  # 登录后带cookie
    res.encoding = res.apparent_encoding
    #print(res.text)
    html = etree.HTML(res.text)
    total = 0  # 总学分绩点
    total_s = 0  # 总学分
    td = 2  # xpath开始的行
    while True:
        try:
            Cname = html.xpath('/html/body/table/tr[{}]/td[1]/text()'.format(td)) [0] # 课程名
            try:
                Ctype = html.xpath('/html/body/table/tr[{}]/td[2]/span/text()'.format(td))[0]  # 课程类型
            except:
                Ctype = 'None'
            score = html.xpath('/html/body/table/tr[{}]/td[5]/text()'.format(td))[0]  # 学分
            try:
                grade = html.xpath('/html/body/table/tr[{}]/td[11]/text()'.format(td))[0]  # 成绩
            except:
                grade='0.0'
            grade = float(grade)
            #print(Cname, Ctype, score, grade)此处不输出，只输出有成绩的课程信息
            td += 1
            if grade != 0.0:#即成绩存在，才会统计在GPA计算中
                score = float(score)
                total_s += score  # 总学分
                if grade >= 90.0:
                    jd = 4.0  # 绩点
                elif grade >= 85.0:
                    jd = 3.7
                elif grade >= 82.0:
                    jd = 3.3
                elif grade >= 78.0:
                    jd = 3.0
                elif grade >= 75.0:
                    jd = 2.7
                elif grade >= 72.0:
                    jd = 2.3
                elif grade >= 68.0:
                    jd = 2.0
                elif grade >= 64.0:
                    jd = 1.5
                elif grade >= 60.0:
                    jd = 1.0
                else:
                    jd = 0.0
                print(Cname, Ctype, score, grade,'该课程绩点为:', jd)
                xfj = jd * score  # 学分绩
                xfj = round(xfj, 2)  # 保留2位小数
                total += xfj  # 总学分绩
        except:
            print('成绩获取完成！')
            break#跳出循环
    GPA = round(total / total_s, 2)#GPA等于总学分绩点/总学分
    print('GPA:', GPA, "总学分绩:",total,'总学分（只包含已公布成绩）:', total_s)

if __name__ == '__main__':
    username = username  # 教务系统账号
    password = 'password'  # 教务系统密码，得是字符
    s, cookie, csrftoken = LoginByPost(username, password)
    ALL_GPA(s, cookie,csrftoken)

