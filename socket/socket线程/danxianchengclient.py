# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 16:16:00 2017

@author: ubuntu
"""
import socket
s=socket.socket()#创建客户机的套接字
address=('127.0.0.1',1234)
s.connect(address)
data='5,6'
s.sendall(data)
datavalue=s.recv(1024)
print 'the result is',datavalue
s.close()
