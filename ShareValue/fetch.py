#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:ros
import config
import time
b=0
# 查看修改后的全局变量
while b<20:
    b = b+1
    time.sleep(1)
    print(config.get_name())