# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 09:05:41 2017

@author: ros
"""

from xmlrpclib import ServerProxy
s=ServerProxy('http://ubuntu:2345/')
caller_id='/teleop_turtle'
topic='/turtle1/cmd_vel'
caller_api='http://ubuntu:5678'
s.publisherUpdate(caller_id, topic, caller_api)