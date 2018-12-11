#!/usr/bin/env python
# coding: utf-8
'''
created in 2018-6-7
利用百度AI的web api实现语音合成:https://ai.baidu.com/docs#/TTS-API/top
'''
import requests
import os
import time
import urllib2
import json

apiKey = "KLB4LNxGRAiX58sBLpZOycEn"
secretKey = "2xCMsnTurRFGTrRZg04UKwYqy9RNsyXK "
auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" \
                        + apiKey + "&client_secret=" + secretKey
res = urllib2.urlopen(auth_url)
json_data = res.read()
token = json.loads(json_data)['access_token']
Mac = "64:00:6A:69:07:E2"
text = "欢迎您使用百度智能语音web api"
base_url = "http://tsn.baidu.com/text2audio"

param_dic = {'tex':text,'ctp':'1','lan':'zh','cuid':Mac,'tok':token}
r = requests.get(url=base_url,params=param_dic,stream=True)
voice_fp = open('/home/ros/tts.wav', 'wb')
voice_fp.write(r.raw.read())
voice_fp.close()
os.system('mplayer /home/ros/tts.wav')

