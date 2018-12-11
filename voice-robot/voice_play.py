#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2018-11-23:利用python播放音频
"""
# author:ros
#-*-coding:utf-8-*-

#引入库
import pyaudio
import wave
import sys
import time
# 定义数据流块
CHUNK = 1024

if __name__ == '__main__':
    # 只读方式打开wav文件
    wf = wave.open(r'/home/ros/10848.wav', 'rb')

    p = pyaudio.PyAudio()

    # 打开数据流
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # 读取数据
    data = wf.readframes(CHUNK)

    # 播放
    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)
    # 停止数据流
    stream.stop_stream()
    stream.close()

    # 关闭 PyAudio
    p.terminate()
