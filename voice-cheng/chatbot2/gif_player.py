# -*- coding: utf-8 -*-
"""
Created on Fri Dec 09 17:22:13 2016

@author: redsun
"""
import sys
import random
from PyQt4.QtCore import *
from PyQt4 import QtGui,uic  
from PyQt4.QtGui import QMainWindow,QLabel,QApplication
from baiduvoice import BaiduVoice
from turing import Turing
from voicedetector import VoiceDetector
import thread  


class GifPlayer(QtGui.QMainWindow):
    def __init__(self, *args):
        super(GifPlayer, self).__init__(*args)
        uic.loadUi('gif_player.ui',self)
        self.connect(self.play,SIGNAL("clicked()"),self.playonce)
        self.timer = QTimer()
        self.timer.timeout.connect(self.blink)
        self.gif_list=['eva_blink.gif','eva_talk.gif','eva_talk_blink.gif','eva_hear_eye_back.gif','eva_hear_eye_move.gif','eva_hearing.gif']
        thread.start_new_thread(self.chatbotThread, ())
        self.state=0 #0 normal, 1 listening, 2, talking
        self.playonce()
        
    def playonce(self):
        if self.timer.isActive() ==False :
            self.timer.start(100*1)#100ms 
        else:
            self.timer.stop()
        
    def blink(self):
        if self.state==0 :
            gif_str="face/"+self.gif_list[0]
        if self.state==1 :
            gif_str="face/"+self.gif_list[5]
        if self.state==2 :
            gif_str="face/"+self.gif_list[random.randint(1,2)]
            
        movie = QtGui.QMovie(gif_str)
        self.player.setMovie(movie)
        movie.start()
        self.timer.stop()
        if self.state==2 :
            self.timer.start(250)#100ms
        else:
            self.timer.start(1000)#100ms
        
    def chatbotThread(self):
        tr=Turing()
        bv=BaiduVoice()
        vd=VoiceDetector()
        while True:
            try:
                self.state=1
                vd.QueryVoice()
                self.state=0
                req=bv.VoiceRecognize()
                print u"你>>>>："+req
                text=tr.QuestionTuring(req)  
                print u"我>>>>："+text
                self.state=2
                bv.TTS_Play(text)
            except:
                text=u"抱歉，我没听清，请再说一次！"
                print u"我回答："+text
                self.state=2
                bv.TTS_Play(text)             
        
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    m_cc=GifPlayer()
    m_cc.show()
    sys.exit(app.exec_())