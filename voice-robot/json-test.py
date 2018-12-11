#!/usr/bin/env python
# coding: utf-8
import json

#json.dumps(python对象)：将python对象转换成json对象
#json.loads(json字符串)：将json字符串还原为python对象
# Python	        JSON
# dict	            object
# list, tuple	    array
# str, unicode	    string
# int, long, float	number
# True	true
# False	false
# None	null

list = [1,2,3,4,5]
dict ={'1':'a','2':'b','3':'c'}
true = True
print (json.dumps(list),type(json.dumps(list)),type(json.loads(json.dumps(list))))
print (json.dumps(dict),type(json.dumps(dict)),type(json.loads(json.dumps(dict))))
print (json.dumps(true),type(json.dumps(true)),type(json.loads(json.dumps(true))))
