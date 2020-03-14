#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : Gary
import pymysql
# python mysql 创建库、表增删改查标准语句
print('----------------------------')
print('载入mysql模块完成')
con = pymysql.connect(host='localhost', user='root',passwd='Xts0916.', charset='utf8')
# con = pymysql.connect(host='localhost', user='root',
# passwd='password', db='test_db',  charset='utf8') # 直接连入db1库
print('创建连接完成')
cur = con.cursor()
print('获取光标完成')
cur.execute("create database flask_demo character set utf8;")
print('创建数据库完成！')
cur.execute("use flask_demo;")
print('进入flask_demo库完成')
cur.execute("CREATE TABLE user_info (username varchar(255) NOT NULL,password varchar(255) DEFAULT NULL,PRIMARY KEY (username)) character set utf8;")
print('创建用户表完成')
cur.execute("INSERT INTO user_info VALUES ('test', 'test');")#可能插入不成功，需要用Navicat手动插入一下，或者直接执行sql文件
print('插入test用户成功！')

