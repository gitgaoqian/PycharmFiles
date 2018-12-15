# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 20:37:24 2017

@author: ros
"""
from xmlrpclib import ServerProxy
s=ServerProxy('http://ubuntu:11311')
caller_id='/turtlesim'#call_id是node名字
topic='/turtle1/cmd_vel'#主题
topic_type='geometry_msgs/Twist'#消息类型
caller_api='http://ubuntu:2345'#该node在何处运行
s.registerSubscriber(caller_id, topic, topic_type, caller_api)




