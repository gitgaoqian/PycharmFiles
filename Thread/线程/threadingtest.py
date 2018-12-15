# -*- coding: UTF-8 -*-
#---- Condition
#---- 捉迷藏的游戏
import os
import threading, time
class Hider(threading.Thread):
    def __init__(self, cond, name):
        super(Hider, self).__init__()
        self.cond = cond
        self.name = name
    
    def run(self):
        time.sleep(1) #确保先运行Seeker中的方法   
        
        self.cond.acquire() #b    
        os.system('python local_launch.py')
        os.system('')
        if hider.is_alive:
            print 'yes'
        else:
            print 'no'
        time.sleep(2)
        self.cond.notify()
        self.cond.wait() 

        
class Seeker(threading.Thread):
    def __init__(self, cond, name):
        super(Seeker, self).__init__()
        self.cond = cond
        self.name = name
    def run(self):
        self.cond.acquire()
        self.cond.wait()    #a    #释放对琐的占用，同时线程挂起在这里，直到被notify并重新占有琐。
                            #d
        os.system('python a.py')
        time.sleep(2)
     
        
cond = threading.Condition()
seeker = Seeker(cond, 'seeker')
hider = Hider(cond, 'hider')
seeker.start()
hider.start()