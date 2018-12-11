# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 16:16:00 2017

@author: ubuntu
"""
import socket
s=socket.socket()#创建客户机的套接字
address=('127.0.0.1',1234)
s.connect(address)
data="中文".encode("utf-8")
print (data)
s.sendall(data)#发送字节(二进制数据)
s.close()
