# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 00:46:20 2016

@author: 程红太
"""
import socket
import thread
from RSVCodec import RSVCodec

class TcpClient:
    HOST = '127.0.0.1'
    PORT = 3000


    def __init__(self, _parent, ipaddr='127.0.0.1', port=3000):
        self.HOST = ipaddr
        self.PORT = port
        self.BUFSIZ = 1024
        self.ADDR = (self.HOST, self.PORT)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.parent = _parent

    def setCodec(self,pre_fix, post_fix, middle_fix, wildcards):
        self.codec = RSVCodec(pre_fix, post_fix, middle_fix, wildcards)

    def start(self):
        try:
            self.client.connect(self.ADDR)
            self.isquit = False
            thread.start_new_thread(self.updateBufferThread, ())
            print "updateBufferThread started..."
            return True
        except:
            return  False

    def stop(self):
        self.client.close()
        if self.isquit==False:
            self.isquit=True
            while self.isquit==True :
                time.sleep(0.1)

    def updateBufferThread(self):
        while self.isquit==False:
            try:
                data = self.client.recv(self.BUFSIZ)
                value=self.codec.decode(data)
                self.parent.refreshObjList(value)
                print value
            except:
                self.parent.offlineCamera()
                self.isquit = True
                return
