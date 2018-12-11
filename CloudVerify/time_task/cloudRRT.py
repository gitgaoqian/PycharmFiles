# -*- coding: utf-8 -*-
"""
Created at 2018-4-17

@author: ros
"""
#定义的rrt时间是:从客户端发送图片到成功接收到处理成功的回复信息.

import flask
import os
import time
import thread

stop_time = 0
break_flag = 0

# start_time=time.time()
def topic_monitor():
    global stop_time
    os.system('rostopic echo /camera/scan > /home/ros/scan.txt')


if __name__ == '__main__':
    thread.start_new_thread(topic_monitor, ())

    while break_flag == 0:
        if os.path.getsize('/home/ros/scan.txt'):
            stop_time = time.time()
            break_flag = 1
            #           interval=stop_time-start_time
            #           print interval
            print stop_time



