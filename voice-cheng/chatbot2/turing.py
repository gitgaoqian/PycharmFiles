# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 14:43:13 2016

@author: 程红太
"""
import json
import httplib, urllib
from baiduvoice import BaiduVoice

class Turing():
    def QuestionTuring(self,sentence):
        req={"key":"88581dfbcb8e49aba08fda8fa274e451","info":sentence,"userid":"redsuncheng"}
        httpClient = None
        try:
            params = urllib.urlencode(req)
            headers = {"Content-type": "application/x-www-form-urlencoded"
                        , "Accept": "text/plain"}
         
            httpClient = httplib.HTTPConnection("tuling123.com", 80, timeout=30)
            httpClient.request("POST", "/openapi/api", params, headers)
            response = httpClient.getresponse()
            s = json.loads(response.read())
            return s["text"]
        
        except Exception, e:
            print e
        finally:
            if httpClient:
                httpClient.close() 

