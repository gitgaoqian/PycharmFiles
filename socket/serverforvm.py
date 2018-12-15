# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 16:09:30 2017

@author: ubuntu
"""
import SocketServer
class myrequesthandle(SocketServer.BaseRequestHandler):  
   
   
     def handle(self):
        print 'get a connection from: ',self.client_address
        while True:
            data=self.request.recv(4096)
            if not data:
                break
            print 'get data: ',data
            action,filename=data.split()
            f=open(filename,'rb')
            while True:
                data=f.read(4096)
                self.request.sendall(data)
if __name__  =='__main__':
     host='219.216.116.135'
     port=1234
     s=SocketServer.ThreadingTCPServer((host,port),myrequesthandle)
     s.serve_forever()
    


