#-*- coding:utf-8 -*-
#记录话题信息
import threading
import time 
import os
class MyThread(threading.Thread): 
        def __init__(self,topic_name):
                threading.Thread.__init__(self)
                self.topic_name = topic_name
        def run(self):
                os.system('rostopic hz '+self.topic_name+'> /home/ros/'+self.topic_name+'.txt')
    
if __name__ == "__main__": 
        t1=MyThread("/camera/left/image_raw")
        t1.setDaemon(True)
        t1.start()
        t2 = MyThread("/camera/scan")
        t2.setDaemon(True)
        t2.start()
        time.sleep(120)