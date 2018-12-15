# -*- coding: utf-8 -*-
import os
import sys
import time
import thread
def fun():
    os.system('rosrun turtlesim turtlesim_node')
thread.start_new_thread(fun,())
time.sleep(10)
thread.exit()

