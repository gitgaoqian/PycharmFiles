# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:08:19 2017

@author: ubuntu
"""

import socket
s=socket.socket()#创建客户机的套接字
address=('127.0.0.1',4444)
s.connect(address)
data='5,6'
s.sendall(data)
datavalue=s.recv(1024)
print 'the result is',datavalue
s.close()
