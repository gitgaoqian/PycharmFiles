# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 18:20:40 2017

@author: ros
"""

import MySQLdb as mdb

conn=mdb.connect(host="127.0.0.1",user="root",db="stu_inf",passwd="ubuntu",charset="utf8")
cur=conn.cursor()
cur.execute('select * from table1')

lines=cur.fetchall()#接收全部的返回结果行.表中记录已经赋值给变量lines了,接下来就是显示他们
for line in lines:
     print line