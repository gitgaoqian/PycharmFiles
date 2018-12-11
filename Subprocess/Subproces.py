
# -*- coding: utf-8 -*-
"""
creat on 201-4-15
"""

#subprocess模块用于创建子进程,利用Poen类,关于类的参数查看:https://blog.csdn.net/gmq_syy/article/details/76855621.
import subprocess
import os
import time
child = subprocess.Popen(["ping","-c","5","www.baidu.com"],stdout=subprocess.PIPE)
print (child.pid) #查看子进程的pid
print (child.poll())#查看child进程的属性
#None —— 子进程尚未结束；==0 —— 子进程正常退出；> 0—— 子进程异常退出，returncode对应于出错码；< 0—— 子进程被信号杀掉了
# child.wait()
# #默认用subprocess.Popen创建的子进程,父进程是不会等待的,所以要想父进程等待子进程退出后才退出,就得使用wait函数,
# #使用wait函数后,主进程会立即阻塞
time.sleep(2)
child.terminate()#终止子进程相当于发送信号 SIGTERM 信号；
child.kill #杀死子进程,相当于发送信号 SIGKILL 信号；
time.sleep(1)
print (child.poll())
print ("child process end")
print("parent process end")