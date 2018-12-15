# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 10:00:33 2017

@author: ubuntu
"""

import socket
host='127.0.0.1'
port=4567
s=socket.socket()
s.connect((host,port))
input_command=raw_input('>>')
s.sendall(input_command)
print 'the command sended'
while 1:#设置循环，用来接收服务端命令执行的结果
    result=s.recv(4096)
    print 'the result is: ',result

