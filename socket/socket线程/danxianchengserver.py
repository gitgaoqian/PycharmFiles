# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 16:15:03 2017

@author: ubuntu
"""

import socket
s=socket.socket()#创建一个socket模块中的socket类的实例对象
#host=socket.gethostname()#利用模块方法获取主机名,这里socket指的是socket
#port=1234
#s.bind((host,port))
address=('127.0.0.1',1234)
s.bind(address)
s.listen(5)
while True:
    c,addr=s.accept()#返回格式为(client,address)的元祖,其中此处命名的client
    #不是客户端而是监听完毕后提供的服务套接字,注意监听套接字和服务套接字
    print 'got the connection from',addr
    data=c.recv(1024)
    if not data:break
    print 'the data from client is',data
    datavalue=data.split(',')
    result=int(datavalue[0])+int(datavalue[1])
    c.sendall(str(result))
    c.close()
