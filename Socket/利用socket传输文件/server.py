# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 16:09:30 2017
updated on 2018-6-13

@author: ubuntu
"""
import chardet
import socketserver
import time
class myrequesthandle(socketserver.BaseRequestHandler):#定义客户端请求处理类
     def recvfile(self):
        f = open("audio2.wav", 'wb')#二进制打开一个file，但此时是空文件，需要写入数据
        # self.request.send('server start recving')#服务套接字向客户端发送“开始接收”
        while True:#设置循环，为了把接受来的数据写入空文件里
            data = self.request.recv(4096)#设置每次从客户端接受最大字节数
            # print(chardet.detect(data))
            if data == b'EOF':#标志接收完毕
                print ("recv file success!")
                break
            f.write(data)#把所偶数据写入文件
        f.close()#关闭文件
     def sendfile(self,filename):
         f=open(filename,'rb')#打开客户端所申请接收的文件
         # self.request.send('server starts sending')
         while True:#设置循环，进行发送文件内容
             data=f.read(4096)#设置读取最大字节数
             if not data:
                 break
             self.request.sendall(data)#发送数据
         f.close()#发送完毕，关闭文件
         time.sleep(1)
         # self.request.send('EOF')#标志位，当客户段收到时，表名客户端接收完毕
         print ('send file successfully')
     def handle(self):#定义handle函数
        print ('get a connection from: ',self.client_address)
        while True:
            data=self.request.recv(4096)#服务端套接字接受传来的命令和文件名
            if not data:
                break
            print ('get data: ',data)
            action = 'send'
            if action == 'send':#若客户端发来的命令是send则服务端就接受文件，进入recvfile函数
                self.recvfile()#注意是self.不是self.request.
            elif action == 'recv':
                self.sendfile()
if __name__  =='__main__':
     host='127.0.0.1'
     port=2222
     s=socketserver.ThreadingTCPServer((host,port),myrequesthandle)
     s.serve_forever()
    
