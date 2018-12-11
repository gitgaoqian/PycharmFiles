#!/usr/bin/env python
# coding: utf-8
'''
created in 2018-6-7
利用百度AI的web api实现语音识别:https://ai.baidu.com/docs#/TTS-API/top
'''
import requests
import time
import json
import base64

token = "24.b7770e1dec06b4d8fe71b9ad34759279.2592000.1530932383.282335-11363408"
Mac = "64:00:6A:69:07:E2"
audio = "/home/ros/asr.wav"
base_url = "http://vop.baidu.com/server_api"
data = {"format": "wav", "rate": 16000, "channel": 1, "token": token, "cuid": Mac, "lan": "zh"}
# 语音的一些参数
wav_fp = open(audio, 'rb')
voice_data = wav_fp.read()#字节型数据
data['len'] = len(voice_data)
data['speech'] = base64.b64encode(voice_data).decode('utf-8')#变成字符型
#从音频文件中读取的是二进制类型数据（字节型），需要把它解码成字符型。但是这里不能直接voice_data.decode('utf-8'),会出错，原因不知
post_data = json.dumps(data).encode('utf-8')
r = requests.post(base_url, data=post_data)
print (r.text)

