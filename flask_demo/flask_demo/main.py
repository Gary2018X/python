#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : Gary
from flask import Flask,render_template, request, url_for, redirect
import pymysql#处理数据库

app = Flask(__name__)#初始化项目
#***************************************************数据库操作**************************************************************#
#2019/12/11更新，只需要传入sql语句，支持大小写,及时关闭数据库链接
def database(sql):
    type = sql.split(' ')[0].lower()
    conn = pymysql.connect(host='127.0.0.1', user='root', password='Xts0916.', db='flask_demo', charset='utf8')  # 连接数据库
    cur = conn.cursor()#用于访问和操作数据库中的数据（一个游标，像一个指针）
    if type=='select':
        cur.execute(sql)  # 执行操作
        result = cur.fetchall()#匹配所有满足的
        conn.close()  # 关闭数据库连接
        return result
    elif type=='insert' or type=='update' or type=='delete':
        try:
            cur.execute(sql)
            conn.commit()#提交事务
            conn.close()  # 关闭数据库连接
            #print("{} ok".format(type))
        except:# 发生错误时回滚
            print('something wrong!')
            conn.rollback()#回滚事务
            conn.close()  # 关闭数据库连接

#*******************网页操作**************************#
# 首页
@app.route('/', methods=['POST','GET'])
def home():
    return render_template('login.html')
#处理登录的路由
@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']#获取账号
        # print(username)
        if username:
            password = request.form['password']#获取密码
            if password:
                try:
                    sql='select password from user_info where username="{}"'.format(username)
                    password_in_db=database(sql)[0][0]#获取存在数据库对应账号的密码
                    if password==password_in_db:  # 检查密码是否正确
                        return render_template('index.html', name=username)  # 登录成功转到需要登录的页面
                        #前端html需要获取到flask传的值用{{变量名}}
                    else:
                        return render_template('login.html', status='fail')  # 用户名或密码错误
                except Exception as e:#所有的异常都归为用户名不存在
                    print(str(e))
                    return render_template('login.html',status='no_exist')#用户名不存在
            else:
                return render_template('login.html', status='null')# 密码为空
        else:
            return render_template('login.html', status='no')# 账号为空
#***************************************************自定义处理错误******************************************************
@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('home'))# return '404 发生页面错误, 未找到内容'，导向登录界面

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5926')  # 启动本地服务
    #app.run(debug=True, host='0.0.0.0', port='5926')  # 启动广域网服务，可以基于ip访问
