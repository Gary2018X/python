# -*- coding: utf-8 -*-
# author:Gary
import requests# 获取网页内容
from lxml import etree# 供xpath解析网页内容
from bs4 import BeautifulSoup#解析网页内容
import re# 正则匹配内容
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
# 获取网页的内容
def get_html(url):
    res=requests.get(url,headers=header)#获取网页，并带有伪装的浏览器头，一般好一朵的网站会有检测是不是程序访问
    res.encoding=res.apparent_encoding#设置编码，防止乱码
    # print(res.text)#输出网页内容
    return res.text#返回网页的内容

#通过bs4解析，主要是标签选择器
def ana_by_bs4(text):
    soup = BeautifulSoup(text, 'html.parser')#注意需要添加html.parser解析
    lis = soup.select("ol li")#选择ol,li标签
    for li in lis:
        index = li.find('em').text#索引
        title = li.find('span', class_='title').text#正标题
        rating = li.find('span', class_='rating_num').text#评分
        try:
            quote=li.find('span',class_='inq').text#名言
        except:
            quote=''
        strInfo = re.search("(?<=<br/>).*?(?=<)", str(li.select_one(".bd p")), re.S | re.M).group().strip()#年份、国家、类型
        infos = strInfo.split('/')
        year = infos[0].strip()#年份
        area = infos[1].strip()#国家，地区
        type = infos[2].strip()#类型
        print(index, title, rating, year, area, type,quote)

#通过xpath解析，主要是路径选择器，可能会受框架影响对应不到内容（tbody）,多层html嵌套
def ana_by_xpath(text):
    # print(text)
    data = etree.HTML(text)#
    for i in range(1,26):# 一页25个数据
        title=data.xpath('//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[1]/a/span[1]/text()'.format(i))[0]#正标题
        try:
            en_title=data.xpath('//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[1]/a/span[2]/text()'.format(i))[0]#英语名
        except:
            en_title=''
        try:
            other = data.xpath('//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[1]/a/span[3]/text()'.format(i))[0]  # 其他标题
        except:
            other=''
        director=data.xpath('//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[2]/p[1]/text()[1]'.format(i))[0]#导演
        strInfo=data.xpath('//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[2]/p[1]/text()[2]'.format(i))[0]#年份地区类型
        infos = strInfo.split('/')
        year = infos[0].strip()  # 年份
        area = infos[1].strip()  # 国家，地区
        type = infos[2].strip()  # 类型
        grade=data.xpath('//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[2]/div/span[2]/text()'.format(i))[0]#评分
        people=data.xpath('//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[2]/div/span[4]/text()'.format(i))[0]#评分人数
        try:
            quote=data.xpath('//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[2]/p[2]/span/text()'.format(i))[0]#名言
        except:
            quote=''
        print('标题:',title,en_title,other)
        print('导演及其主演:',director.strip())
        print('年份、国家地区、类型:',year,area,type)
        print('评分以及评分人数:',grade,people)
        print('名言:',quote.strip())



if __name__ == '__main__':
    for page in range(10):
        print('第{}页'.format(page+1))
        url='https://movie.douban.com/top250?start={}&filter='.format(page*25)#电影的url，有多页的时候需要观察url的规律
        text=get_html(url)# 获取网页内容
        # ana_by_bs4(text)# bs4方式解析
        ana_by_xpath(text)# xpath 方式解析
