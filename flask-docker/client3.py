# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:06:17 2017

@author: ros
"""
import requests,json
value={'value':'robot/video'}
headers={'content-type': 'application/json'}
r = requests.post("http://127.0.0.1:5566/robotinfo",data=json.dumps(value),headers=headers)
print r.headers
print r.json()




