# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 20:48:01 2017

@author: ubuntu
"""

from glanceclient import client
glance = client.Client("2", "admin", "admin", "admin", "http://172.16.0.2:5000/v2.0")
