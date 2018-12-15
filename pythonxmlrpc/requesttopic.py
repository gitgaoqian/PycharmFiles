# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 09:10:14 2017

@author: ros
"""
from xmlrpclib import ServerProxy
s=ServerProxy('http://ubuntu:5678/')
caller_id='/turtlesim'
topic='/turtle1/cmd_vel'
protocols=[['TCPROS']]
s.requestTopic(caller_id, topic, protocols)
