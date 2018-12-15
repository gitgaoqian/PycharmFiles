# -*- coding: UTF-8 -*-
#实现线程的切换，但是每个子线程必须使用手动ctrl+c才能取消，也才能切换到另一个线程
import os
import threading, time
class Add(threading.Thread):
    def __init__(self, cond, data):
        super(Add, self).__init__()
        self.cond = cond
        
        self.data=data
    
    def run(self):
        while 1:
            time.sleep(1) #确保先运行Seeker中的方法   
        
            self.cond.acquire() #b    
            #result=self.data[0]+self.data[1]
            #print result
            os.system("python a.py")
            #2s后唤醒挂起的除法线程,本线程进入等待
            time.sleep(2)
            self.cond.notify()
            self.cond.wait()
       
class Div(threading.Thread):
    def __init__(self, cond, data):
        super(Div, self).__init__()
        self.cond = cond
        
        self.data=data
    
    def run(self):
        while 1:
            #挂起线程，待唤醒后，执行除法
            self.cond.acquire()
            self.cond.wait()
            #result=self.data[0]/self.data[1]
            #print result
            os.system('python b.py')
            #2s后唤醒加法线程
            time.sleep(2)
            self.cond.notify()
            
                    
cond = threading.Condition()

add = Add(cond,(6,2))
div=Div(cond,(6,2))
add.start()
div.start()
time.sleep(10000)
