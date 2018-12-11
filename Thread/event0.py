# coding: utf-8
from threading import Thread,Event
import time
def test_event(e):
    while 1:
        print("run...")
        e.wait()
        time.sleep(1)
if __name__=='__main__':
    e = Event()
    t = Thread(target=test_event,args=(e,))
    t.start()
    e.set() #初始e.set说明标志位为True,函数中的e.wait不会阻塞
    time.sleep(2)
    e.clear()#e.clear说明标志位为False,函数中的e.wait此时处于阻塞.
    time.sleep(5)
    e.set()
    print ('over')