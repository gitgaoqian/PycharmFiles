# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 10:03:51 2017

@author: ubuntu
"""

import socket
import subprocess
host='127.0.0.1'
port=4567
s=socket.socket()
s.bind((host,port))
s.listen(5)
while 1:
    ss,addr=s.accept()
    while True:
        data=ss.recv(4096)
        if not data:
            break
        print 'recv the command is: ',data
        handle=subprocess.Popen(data,shell=True,stdout=subprocess.PIPE)
        #创建子进程用来执行客户端发来的命领，第一个参数是接收到的命令，字符串格式，第二个参数定义shell
        #执行，最后一个参数定义执行完毕后的标准输出文件
        out=handle.stdout.readlines()
        for line in out:#把执行完毕的结果发送给客户端
            ss.sendall(line)
        ss.send('the job is finished')