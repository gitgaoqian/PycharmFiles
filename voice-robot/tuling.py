#!/usr/bin/env python
# coding: utf-8
'''
created in 2018-6-7
利用图灵机器人的web api实现聊天功能(语义理解):https://segmentfault.com/a/1190000013900291
'''
import json
import urllib3.request
import requests

api_url = "http://openapi.tuling123.com/openapi/api/v2"
text_input = input('我：')

req = {
    "perception":
    {
        "inputText":
        {
            "text": text_input
        },

        "selfInfo":
        {
            "location":
            {
                "city": "沈阳",
                "province": "辽宁",
                "street": "文化路"
            }
        }
    },

    "userInfo":
    {
        "apiKey": "3aa5231887234e20b7867a3c656941da",
        "userId": "OnlyUseAlphabet"
    }
}
# 将字典格式的req编码为utf8
req_data = json.dumps(req).encode('utf8')
response = requests.post(api_url, data=req_data, headers={'content-type': 'application/json'})
data = response.json()
result = data['results'][0]['values']['text']
print (result)

