# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 16:25:37 2017

@author: ubuntu
"""
#能够会利用socket传递文本，图片以及音频.好像都差不多。主要就是python内部就解决了图片，语音文件的编码，但是我们不知到如何编码的
import socket
import time
host= '127.0.0.1'
port=2222
s=socket.socket()
def sendfile (filename):
    f=open(filename,'rb')#创建文件操作对象，并以二进制方式打开file
    while True:#若打开文件成功，设置循环进行发送文件内容
        data=f.read(4096)#定义每次最大读取的字节数
        if not data:
            break
        s.sendall(data)#客户端发送文件内的内容
    f.close()#发送完毕，关闭文件
    time.sleep(1)
    s.sendall('EOF'.encode('utf-8'))#发送一个标志，若客户端收到则证明客户端接受成功
    print ('send successfully！')
def recvfile (filename):
    f=open(filename,'wb')#打开file为空文件
    while True:#设置循环写入文件内容
        data=s.recv(4096)#设置每次从服务端接收最大字节数
        if data == b'EOF':
            print ('recving successflully')
        f.write(data)#写入文件数据
    f.close()
    
s.connect((host,port))
while True:
    client_command=input('>> ')#输入命令和文件名字中间用空格隔开
    if not client_command:
        continue
    s.sendall(client_command.encode("utf-8"))
    action,filename=client_command.split()
    print ('action ' ,action)
    print ('filename',filename)
    time.sleep(1)
    if action=='send':
        print ('client send file to server')
        sendfile(filename)#客户端主动发送文件，进入sendfile函数
    elif action == 'recv':
        print ('client recv file from server')
        recvfile(filename)#客户端申请接收服务端文件
