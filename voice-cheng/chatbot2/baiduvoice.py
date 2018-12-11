# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 15:59:57 2016

@author: 程红太
"""
import wave  
import urllib2, pycurl 
import json 
#import mp3play
import sys
import time
import re
import os

class BaiduVoice():
    def __init__(self):
        reload(sys)
        sys.setdefaultencoding( "utf-8" )
        self.token=self.get_token()
        self.cuid="50-1A-C5-EE-9B-BF"
    def TTS_Play(self,text):
        text = text.decode("utf8")
        string=text
        string = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode("utf8"), ",".decode("utf8"),text)
        srv_url ='http://tsn.baidu.com/text2audio?tex='+string+'&lan=zh&cuid='+self.cuid+'&ctp=1&tok='+self.token
        f = urllib2.urlopen(srv_url) 
        print 'mp3 returned'
        data = f.read()
        with open('temp.mp3', "wb") as code:     
            code.write(data)
        # clip = mp3play.load('temp.mp3')
        # clip.play()
        # time.sleep(clip.seconds()+1)
        # clip.stop()
        os.system("mplayer temp.mp3")
        
    ## get access token by api key & secret key  
    def get_token(self):  
        #return '24.80f11ca07249e2e55168104b2dc4767e.2592000.1482501543.282335-8933830'
        apiKey = "DYb1gvPy38KEsLMcXLVmL5Yb"  
        secretKey = "3dc95ba0edc0d1ffee60a1ff1c0677a8"  
        auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey;  
        res = urllib2.urlopen(auth_url)  
        json_data = res.read()  
        print json_data
        return json.loads(json_data)['access_token']  
    def dump_res(self,buf):  
        self.response=buf          
    ## post audio to server  
    def VoiceRecognize(self):  
        fp = wave.open('temp.wav', 'rb')  
        nf = fp.getnframes()  
        f_len = nf * 2  
        audio_data = fp.readframes(nf)  
      
        cuid = "50-1A-C5-EE-9B-BF"
        srv_url = 'http://vop.baidu.com/server_api' + '?cuid=' + cuid + '&token=' + self.token  
        http_header = [  
            'Content-Type: audio/pcm; rate=8000',  
            'Content-Length: %d' % f_len  
        ]  
      
        c = pycurl.Curl()  
        c.setopt(pycurl.URL, str(srv_url)) #curl doesn't support unicode  
        c.setopt(c.HTTPHEADER, http_header)   #must be list, not dict  
        c.setopt(c.POST, 1)  
        c.setopt(c.CONNECTTIMEOUT, 30)  
        c.setopt(c.TIMEOUT, 30)  
        c.setopt(c.WRITEFUNCTION, self.dump_res)  
        c.setopt(c.POSTFIELDS, audio_data)  
        c.setopt(c.POSTFIELDSIZE, f_len)  
        
        print "recognizing..."
        c.perform() #pycurl.perform() has no return val
        s = json.loads(self.response)
        return s["result"][0].encode("UTF-8")
    
if __name__ == "__main__":  
    tts=BaiduVoice()
    text= tts.VoiceRecognize()
    print text