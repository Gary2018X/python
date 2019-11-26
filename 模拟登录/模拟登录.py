import requests

header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}
login_url='https://accounts.douban.com/j/mobile/login/basic'#登录的url
data={'ck': '',
'name':'15623252882',
      'password':'Xts0916.',
"remember": "false",
"ticket":''}
s=requests.session()#作用是跨请求保持参数，也就是说s这个session对象所发出的所有请求之间会保持cookies
s.post(login_url,data,headers=header)#发送登录信息

url='https://www.douban.com/'#获取登录进去的首页
res=s.get(url,headers=header)#获取自己的首页
res.encoding='utf-8'
print(res.text)