# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 08:29:18 2017

@author: ros
"""

import requests

user_info = {'name': 'letian', 'password': '123'}
r = requests.post("http://127.0.0.1:5566/register", data=user_info)

