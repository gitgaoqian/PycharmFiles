# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 08:57:30 2017

@author: ros
"""

from flask import Flask, request, Response
import json

app = Flask(__name__)



@app.route('/addition',methods=['POST'])
def add():
    
     value1=request.json['a']
     value2=request.json['b']
     value=value1+value2
     value={'value':value}#形成一个python字典对象
     response=Response(json.dumps(value),  mimetype='application/json')
     #将python对象编码成json字符串并同http响应头一同返回给客户端
     response.headers.add('server','python flask')
     return response
    
if __name__ == '__main__':
    app.run('127.0.0.1',5566)
