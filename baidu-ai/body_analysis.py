#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:ros
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:ros
import requests
import urllib2
import json
import base64
import urllib
import cv2
class BodyAnalysis:
    def __init__(self):
        self.api_key = 'q63nV6pfd7HYET1nwZqkuwCQ'
        self.secret_key = 'LGVb0uPtZHuXpNlcNwD3QaNqdYAW94Mr'
        self.auth_url = self.auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" \
                                        + self.api_key + "&client_secret=" + self.secret_key
        self.key_point_url = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/body_analysis'
        self.attr_url = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/body_attr'
        self.num_url = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/body_num'
        self.token = self.GetToken()
    def GetToken(self):
        res = urllib2.urlopen(self.auth_url)
        data = res.read()
        return json.loads(data)['access_token']
    def KeyPointDetect(self):
        f = open('/home/ros/baidu_ai/person.jpg', 'rb')
        img = base64.b64encode(f.read())

        params = {"image": img, "access_token": self.token}
        params = urllib.urlencode(params)

        request = urllib2.Request(url=self.key_point_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib2.urlopen(request)
        content = response.read()
        if content:
            print content
    def AttributeDetect(self):
        f = open('/home/ros/baidu_ai/person.jpg', 'rb')
        img = base64.b64encode(f.read())

        params = {"image": img,"access_token": self.token}
        params = urllib.urlencode(params)

        request = urllib2.Request(url=self.attr_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib2.urlopen(request)
        content = response.read()
        if content:
            print content
    def BodyNumDetect(self):
        f = open('/home/ros/baidu_ai/person.jpg', 'rb')
        img = base64.b64encode(f.read())

        params = {"image": img,"show":True, "access_token": self.token}
        params = urllib.urlencode(params)

        request = urllib2.Request(url=self.num_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib2.urlopen(request)
        content = response.read()
        content = json.loads(content)
        if content:
             print content['person_num']
        f = open('/home/ros/baidu_ai/person1.jpeg','wb')
        f.write(content['image'].decode('base64'))
        f.close()

if __name__ == "__main__":
    body = BodyAnalysis()
    #body.KeyPointDetect()
    #body.AttributeDetect()
    #body.BodyNumDetect()