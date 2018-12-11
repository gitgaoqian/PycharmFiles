# -*- coding: utf-8 -*-
"""
creat on 201-4-15
"""
import subprocess
import shlex
import time
def TopicHzCheck():
    cmdstr = "rostopic hz /camera/left/image_raw __name:=topichz"
    cmdlist = shlex.split(cmdstr)#将命令字符串转换成列表
    child = subprocess.Popen(cmdlist,stdout=subprocess.PIPE)
    print (child.pid)
    time.sleep(2)
    child.terminate()
    child.kill
    while 1:
        if child.poll() != None:
            print (child.poll())
            print("child process end")
            break
    #当子进程退出后,读取子进程管道输出
    file = child.stdout.read()
    print (file)
print ("parent process end")


