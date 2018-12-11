# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 08:57:52 2017

@author: ros
"""
import requests, json
value={'a':12,'b':14}
headers = {'content-type': 'application/json'}#设置http请求头为'application/json'
r = requests.post("http://127.0.0.1:5566/addition", data=json.dumps(value), headers=headers)
#利用python中的json.dump是()将 Python 对象编码成 JSON 字符串
print r.headers#读取服务端的http响应头
dic=r.json()#读取服务端响应的json数据(已经解析为python对象了)
dic=2*dic['value']
print dic


