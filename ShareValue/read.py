#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:ros
import time
while True:
    with open("value",'r') as f:
        readBytes = f.read()
        print readBytes
        time.sleep(1)