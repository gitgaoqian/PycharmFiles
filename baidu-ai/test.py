#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:ros
import requests
import urllib2
import json
import base64
import urllib
import cv2
import numpy as np
import time
import threading
import os
global w_flag
global r_flag
class ImageDetect:
    def __init__(self):
        self.api_key = 'cc4xT4PcIR3oaqiTqRBn2EM6'
        self.secret_key = 'eB4wzZbqa2MAS61Vdp6vU5LjRMygtw4i'
        self.auth_url = self.auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" \
                                        + self.api_key + "&client_secret=" + self.secret_key
        self.advance_general_url = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general'
        self.object_detect_url = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/object_detect'
        self.dish_url = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/dish'
        self.car_url = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/car'
        self.logo_url = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/logo'
        self.animal_url = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/animal'
        self.plant_url = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/plant'
        self.ingredient_url = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/classify/ingredient'
        self.token = self.GetToken()
    def GetToken(self):
        res = urllib2.urlopen(self.auth_url)
        data = res.read()
        return json.loads(data)['access_token']
    def AdvanceGeneral(self):#返回图像内容的百度百科内容，对于公众人物、果蔬、动物等有很高识别率，但是对于书籍、电影、电视剧不会识别出这是啥书，那是啥电影.每天有限定的访问次数：
        global w_flag
        global r_flag
        while True:
            if w_flag == 0:
                r_flag = 1
                print ("read image")
                f = open('/home/ros/baidu_ai/frame.jpg', 'rb')
                img = base64.b64encode(f.read())
                params = {"image": img,"baike_num": 1, "access_token": self.token}
                params = urllib.urlencode(params)
                request = urllib2.Request(url=self.advance_general_url, data=params)
                request.add_header('Content-Type', 'application/x-www-form-urlencoded')
                response = urllib2.urlopen(request)
                content = response.read()
                if content:
                    print content
                print("read over")
                r_flag = 0
                time.sleep(0.1)
                f.close()

    def BodyDetect(self):
        # 二进制方式打开图片文件
        f = open('/home/ros/baidu_ai/banana.jpg', 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img, "with_face": 0,"access_token":self.token}

        params = urllib.urlencode(params)
        request = urllib2.Request(url=self.object_detect_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib2.urlopen(request)
        content = response.read()
        if content:
            print content
    def DishDetect(self):
        f = open('/home/ros/baidu_ai/dish.jpg','rb')
        img = base64.b64encode(f.read())
        requst_params = {"image":img,"filter_threshold":0.95,"access_token":self.token}

        request_params = urllib.urlencode(requst_params)
        request = urllib2.Request(url=self.dish_url, data=request_params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib2.urlopen(request)
        content = response.read()
        if content:
            print content
    def CarDetect(self):
        f = open('/home/ros/baidu_ai/car.jpg', 'rb')
        img = base64.b64encode(f.read())

        params = {"image": img, "top_num": 5,"access_token":self.token}
        params = urllib.urlencode(params)

        request = urllib2.Request(url=self.car_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib2.urlopen(request)
        content = response.read()
        if content:
            print content
    def LogoDetect(self):
        f = open('/home/ros/baidu_ai/logo.jpg', 'rb')
        img = base64.b64encode(f.read())

        params = {"image": img, "custom_lib":True, "access_token": self.token}
        params = urllib.urlencode(params)

        request = urllib2.Request(url=self.logo_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib2.urlopen(request)
        content = response.read()
        if content:
            print content
    def AnimalDetect(self):
        f = open('/home/ros/baidu_ai/animal.jpg', 'rb')
        img = base64.b64encode(f.read())

        params = {"image": img, "top_num": 6,"baike_num":0, "access_token": self.token}
        params = urllib.urlencode(params)

        request = urllib2.Request(url=self.animal_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib2.urlopen(request)
        content = response.read()

        if content:
            print content
    def PlantDetect(self):
        f = open('/home/ros/baidu_ai/plant.jpg', 'rb')
        img = base64.b64encode(f.read())

        params = {"image": img, "baike_num": 0, "access_token": self.token}
        params = urllib.urlencode(params)

        request = urllib2.Request(url=self.plant_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib2.urlopen(request)
        content = response.read()
        if content:
            print content
    def IngredientDetect(self):
        f = open('/home/ros/baidu_ai/ingredient.jpg', 'rb')
        img = base64.b64encode(f.read())

        params = {"image": img, "baike_num": 0, "access_token": self.token}
        params = urllib.urlencode(params)

        request = urllib2.Request(url=self.ingredient_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib2.urlopen(request)
        content = response.read()
        if content:
            print content



if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    cap.set(cv2.cv.CV_CAP_PROP_FPS, 10)
    image_detect = ImageDetect()
    T = threading.Thread(target=image_detect.AdvanceGeneral, args=())
    flag = 1
    global w_flag
    global r_flag
    w_flag = 1
    r_flag = 0
    while (True):
        if flag:
            T.start()
            flag = 0
        # Capture frame-by-frame
        ret, frame_array = cap.read()
        # frame_str = np.array2string(frame_array)
        if r_flag == 0:
            print ("write image")
            w_flag = 1
            cv2.imwrite("/home/ros/baidu_ai/frame.jpg",frame_array)
        #image_detect.AdvanceGeneral()
        # Display the resulting frame
            cv2.imshow('image', frame_array)
            print("wirte over")
            w_flag = 0
            time.sleep(0.2)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # image_detect = ImageDetect()
    # image_detect.AdvanceGeneral()
    #image_detect.BodyDetect()
    # image_detect.DishDetect()
    #image_detect.CarDetect()
    #image_detect.LogoDetect()
    # image_detect.AnimalDetect()
    #image_detect.PlantDetect()
    # image_detect.IngredientDetect()