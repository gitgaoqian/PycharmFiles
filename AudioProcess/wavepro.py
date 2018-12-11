#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:ros
#该程序主要是为了对两个库文件：pyaudio和wave进行理解;
# WAV是Microsoft开发的一种声音文件格式，虽然它支持多种压缩格式，不过它通常被用来保存未压缩的声音数据（PCM脉冲编码调制)。WAV有三个重要的参数：声道数、取样频率和量化位数。
# 声道数：可以是单声道或者是双声道
# 采样频率：一秒内对声音信号的采集次数，常用的有8kHz, 16kHz, 32kHz, 48kHz, 11.025kHz, 22.05kHz, 44.1kHz
# 量化位数：用多少bit表达一次采样所采集的数据，通常有8bit、16bit、24bit和32bit等几种
# wave data get  -xlxw

import wave as we
import numpy as np
import matplotlib.pyplot as plt


def wavread(path):
    wavfile = we.open(path, "rb")
    params = wavfile.getparams()
    framesra, frameswav = params[2], params[3]
    datawav = wavfile.readframes(frameswav)
    wavfile.close()
    datause = np.fromstring(datawav, dtype=np.short)
    datause.shape = -1, 2
    datause = datause.T
    time = np.arange(0, frameswav) * (1.0 / framesra)
    return datause, time


def main():
    path = "/home/ros/voice/night.wav"
    wavdata, wavtime = wavread(path)
    plt.title("Night.wav's Frames")
    plt.subplot(211)
    plt.plot(wavtime, wavdata[0], color='green')
    plt.subplot(212)
    plt.plot(wavtime, wavdata[1])
    plt.show()


main()