import socket   #socket模块
import thread
from RSVCodec import RSVCodec
from rsvconfig import RsvConfigure

class TCPServer(object):
    """description of class"""
    def __init__(self, ip_addr, port):
        self.HOST=ip_addr
        self.PORT=port
        self.isconnected=False
        self.s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #定义socket类型，网络通信，TCP
        self.s.bind((self.HOST,self.PORT))   #套接字绑定的IP与端口
        rsvcfg =  RsvConfigure()
        self.codec = RSVCodec(rsvcfg.prefix, rsvcfg.postfix, rsvcfg.middlefix, rsvcfg.wildcards)
        thread.start_new_thread(self.CommunicationThread, ())
   
    def SocketTransfer(self,objlist):
        tcpdata=self.codec.encode(objlist)
        try:
            print tcpdata
            self.conn.sendall(tcpdata)
        except:
            print "Error connection!"
            return
    
    def CommunicationThread(self):
        self.s.listen(1)         #开始TCP监听         
        print "Waiting for the incoming connections"        
        while 1:
            try:
               self.conn,self.addr=self.s.accept()   #接受TCP连接，并返回新的套接字与IP地址
               print'Connected by',self.addr    #输出客户端的IP地址
               self.isconnected=True
               while 1:
                   try:
                       data=self.conn.recv(1024)    #把接收的数据实例化
                       cmd_result=data+" received\n"
                       self.conn.sendall(cmd_result)   #否则就把结果发给对端（即客户端）
                   except:
                       print "connection closed"
                       self.isconnected=False
                       break     
            except:
               print "socket closed"
               self.isconnected=False
               break                     
                
        self.conn.close()     #关闭连接
        print "socket communication closed."
