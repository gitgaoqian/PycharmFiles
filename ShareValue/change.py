#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:ros
import config
import time
# 修改全局变量
a = 0
while a<10:
    time.sleep(1)
    a=a+1
    config.set_name('new_name')
    print (config.get_name())

