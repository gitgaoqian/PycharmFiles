# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 22:26:25 2016

@author: 程红太
"""

from baiduvoice import BaiduVoice
from turing import Turing
from voicedetector import VoiceDetector
tr=Turing()
bv=BaiduVoice()
vd=VoiceDetector()

while True:
    try:
        vd.QueryVoice()
        req=bv.VoiceRecognize()
        print u"你>>>>："+req
        text=tr.QuestionTuring(req)  
        print u"我>>>>："+text
        bv.TTS_Play(text)
    except:
        text=u"抱歉，我没听清，请再说一次！"
        print u"我回答："+text
        bv.TTS_Play(text)        