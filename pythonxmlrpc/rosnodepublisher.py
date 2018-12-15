# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 10:54:20 2017

@author: ros
"""
from xmlrpclib import ServerProxy
s=ServerProxy('http://ubuntu:11311/')
caller_id1='/teleop_turtle'
topic1='/turtle1/cmd_vel'
topic_type1='geometry_msgs/Twist'
caller_api1='http://ubuntu:5678'
s.registerPublisher(caller_id1, topic1, topic_type1, caller_api1)

