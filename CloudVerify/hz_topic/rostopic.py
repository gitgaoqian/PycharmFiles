#!/usr/bin/env python
# coding: utf-8
'''
created at 2018-4-12
'''
# import os
# import thread
# import time
# def hzcheck():
#     os.system("rostopic hz /turtle1/pose __name:=topichz")
# thread.start_new_thread(hzcheck,())
# time.sleep(1)
# os.system("rosnode kill topichz")

#------------------------updated at 2018-4-14:设置守护线程保证子线程退出后主线程才退出----------------------#
# import os
# from threading import Thread
# import sys
# import time
# def hzcheck():
#     os.system("rostopic hz /camera/left/image __name:=topichz")
# if __name__ == '__main__':
#     t = Thread(target=hzcheck, name="topichz")
#     t.setDaemon(True)
#     t.start()
#     time.sleep(30)
#     os.system("rosnode kill topichz")
#     time.sleep(1)
#------------------updated at 2018-4-15:利用子进程模块subprocess进行处理
import subprocess
import shlex
import time
cmdstr = "rostopic hz /camera/left/image __name:=topichz"
cmdlist = shlex.split(cmdstr)#将命令字符串转换成列表
child = subprocess.Popen(cmdlist,stdout=subprocess.PIPE)
#print (child.pid)
time.sleep(2)
child.terminate()
child.kill
while 1:
    if child.poll() != None:
        #print (child.poll())
        #print("child process end")
        break
#当子进程退出后,读取子进程管道输出
file = child.stdout.read()
print (file)
print ("parent process end")
