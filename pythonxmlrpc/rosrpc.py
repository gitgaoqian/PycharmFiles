# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 15:39:08 2017

@author: ros
"""
from xmlrpclib import ServerProxy
#注册订阅节点
s=ServerProxy('http://ubuntu:11311/')
caller_id='/turtlesim'#call_id是node名字
topic='/turtle1/cmd_vel'#主题
topic_type='geometry_msgs/Twist'#消息类型
caller_api='http://ubuntu-desktop:2345'#该node在何处运行
s.registerSubscriber(caller_id, topic, topic_type, caller_api)
#注册发布节点
caller_id1='/teleop_turtle'
topic1='/turtle1/cmd_vel'
topic_type1='geometry_msgs/Twist'
caller_api1='http://ubuntu:5678'
s.registerPublisher(caller_id1, topic1, topic_type1, caller_api1)






