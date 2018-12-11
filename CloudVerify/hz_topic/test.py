#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
from threading import Thread
rdst = None
def hzcheck():
    global rdst
    hz = os.popen('rostopic hz /turtle1/pose __name:=rostopichz')
    while 1:
        if "min" in hz.readline():
            list = hz.readline().split(" ")
            rdst = float(list[2].strip('\n'))
            os.system("rosnode kill /rostopichz")
            #print rdst
def TopicHzCheck():
    global rdst
    t = Thread(target=hzcheck,args=())
    t.setDaemon(True)
    t.start()
    time.sleep(5)
    return rdst
if __name__ == "__main__":
    rdst= TopicHzCheck()
    print rdst