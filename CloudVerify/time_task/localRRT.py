# -*- coding: utf-8 -*-
"""
Created at 2018-4-17

@author: ros
"""

import os
import time
import thread

stop_time = 0
break_flag = 0
start_time = time.time()


def topic_monitor():
    global stop_time
    os.system('rostopic echo /camera/scan > /home/ros/scan.txt')


if __name__ == '__main__':
    thread.start_new_thread(topic_monitor, ())

    while break_flag == 0:
        if os.path.getsize('/home/ros/scan.txt'):  # 判断"/home/ros/scan/txt"是否为空,如果不是,停止计时
            stop_time = time.time()
            break_flag = 1
            interval = stop_time - start_time
        　print interval




