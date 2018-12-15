#!/usr/bin/python
# -*- coding: UTF-8 -*-

import thread
import time
import os

# 为线程定义一个函数
def cloud_launch( threadName):
  
   print "%s" % ( threadName, )
   os.system('python cloud_launch.py')
   time.sleep(1)
   if count>5:
       thread.exit()

def local_launch( threadName):
  
   print "%s" % ( threadName, )
   os.system('python local_launch.py')
   if count<5:
       thread.exit()
# 创建两个线程
    
try:
     count = 0
     if count>5:
         
         
         thread.start_new_thread( local_launch, ("local_launch",  ) )
         
     else:
        
         thread.start_new_thread( cloud_launch, ("cloud_launch",  ) )
         time.sleep(2)
         thread.exit()

except:
     thread.start_new_thread( cloud_launch, ("cloud_launch",  ) )



