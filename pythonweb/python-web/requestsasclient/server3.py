# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 10:55:44 2017

@author: ros
"""


from flask import Flask, request, Response
import json
#josn的数组和键值对形式,建一个组,
group={"group":{"name":"robot","resources":["robot/motion","robot/voice","robot/vision"]}}
app = Flask(__name__)
@app.route('/robotinfo',methods=['GET','POST'])
def mygroup():
    add=request.json['value']
    l=group['group']['resources']
    l.append(add)
    return Response(json.dumps(group),mimetype='application/json')    
if __name__ == '__main__':
    app.run('127.0.0.1',5566)
    
