#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:ros
import time
for i in range(1,100,1):
    f = open('value',"w")
    print i
    f.write(str(i))
    f.flush()
    f.close()
    time.sleep(1)