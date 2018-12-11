#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:ros
import  threading
import time
global w_flag
global r_flag
class FUN:
    def fun(self):
        while True:
            global w_flag
            global r_flag
            if w_flag == 0:
                r_flag = 1
                print("read begin")
                f = open("/home/ros/a.txt",'r')
                print (f.read())
                r_flag = 0
                print("read over")
                time.sleep(2)
                f.close()
def fun2():
    global r_flag
    while True:
        r_flag = 0
        time.sleep(5)
        r_flag = 1
        time.sleep(5)
if __name__ == '__main__':
    f = FUN()
    t1= threading.Thread(target=f.fun,args=())
    # t1.start()
    t2 = threading.Thread(target=fun2,args=())
    t2.start()
    global r_flag
    global w_flag
    r_flag = 0
    w_flag = 1
    while True:
        if r_flag == 0:
            w_flag = 1
            print("wirte begin")
            f = open("/home/ros/a.txt",'w')
            f.write("abc\n")
            print("write over")
            w_flag = 0
            time.sleep(1)
            f.close()
            r_flag = 1
        if r_flag == 1:
            print("read begin")
            f = open("/home/ros/a.txt",'r')
            print(f.read())
            print("read over")
            time.sleep(1)
            f.close()

#-----------线程同步机制测试--------------------------------------
#-------------------lock test--------------- -----
# import threading
# import time
# value = 0
# lock = threading.Lock() #创建一个全局锁对象
# def threadfun(name):
#     global value
#     thread_name = name
#     while value < 10:
#         value = value+1
#         lock.acquire()  # 获取锁
#         print(thread_name+"acquire the lock")
#         print(thread_name+" " + str(value))
#         lock.release() #释放锁
#         print(thread_name+"release the lock")
#         time.sleep(1)
# if __name__ == '__main__':
#     t1= threading.Thread(target=threadfun,args=("thread_1",))
#     t2 = threading.Thread(target=threadfun,args=("thread_2",))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     while value > 5:
#         value = value-1
#         print("main thread:"+str(value))
#         time.sleep(1)

#--------------信号量test-生产者和消费者--------------
# -*- coding: utf-8 -*-
# import threading
# import time
# import random
# semaphore = threading.Semaphore(0)
#
# def consumer():
#         print("consumer is waiting.")
#         # Acquire a semaphore
#         semaphore.acquire()
#         # The consumer have access to the shared resource
#         print("consumed item number %s " % item)
#
# def producer():
#         global item
#         time.sleep(2)
#         # create a random item
#         item = random.randint(0, 1000)
#         print("produced item number %s" % item)
#          # Release a semaphore, incrementing the internal counter by one.
#         # When it is zero on entry and another thread is waiting for it
#         # to become larger than zero again, wake up that thread.
#         semaphore.release()
#
# if __name__ == '__main__':
#         for i in range (0,5) :
#                 t1 = threading.Thread(target=producer)
#                 t2 = threading.Thread(target=consumer)
#                 t1.start()
#                 t2.start()
#                 t1.join()
#                 t2.join()
#         print("program terminated")
#--------------条件变量测试----------------------
# from threading import Thread, Condition
# import time
#
# items = []
# condition = Condition()
#
# class consumer(Thread):
#
#     def __init__(self):
#         Thread.__init__(self)
#
#     def consume(self):
#         global condition
#         global items
#         condition.acquire()
#         print("consumer acquire relock")
#         if len(items) == 0:
#             condition.wait()
#             print("Consumer notify : no item to consume")
#         items.pop()
#         print("Consumer notify : consumed 1 item")
#         print("Consumer notify : items to consume are " + str(len(items)))
#
#         condition.notify()
#         condition.release()
#         print("consumer release relock")
#
#     def run(self):
#         for i in range(0, 10):
#             time.sleep(2)
#             self.consume()
#
# class producer(Thread):
#
#     def __init__(self):
#         Thread.__init__(self)
#
#     def produce(self):
#         global condition
#         global items
#         condition.acquire()
#         print("producer acquire relock")
#         if len(items) == 10:
#             condition.wait()
#             print("Producer notify : items producted are " + str(len(items)))
#             print("Producer notify : stop the production!!")
#         items.append(1)
#         print("Producer notify : total items producted " + str(len(items)))
#         condition.notify()
#         condition.release()
#         print("producer release relock")
#
#     def run(self):
#         for i in range(0, 10):
#             time.sleep(1)
#             self.produce()
#
# if __name__ == "__main__":
#     producer = producer()
#     consumer = consumer()
#     producer.start()
#     consumer.start()
#     producer.join()
#     consumer.join()
#----------------------事件event测试------------------------------
# import time
# from threading import Thread, Event
# import random
# items = []
# event = Event()
#
# class consumer(Thread):
#     def __init__(self, items, event):
#         Thread.__init__(self)
#         self.items = items
#         self.event = event
#
#     def run(self):
#         while True:
#             print("consumer notify:consumer waiting for event set")
#             self.event.wait()
#             print("consumer notify:event set by producer")
#             item = self.items.pop()
#             print('Consumer notify : %d popped from list by %s' % (item, self.name))
#             time.sleep(2)
#
# class producer(Thread):
#     def __init__(self, integers, event):
#         Thread.__init__(self)
#         self.items = items
#         self.event = event
#
#     def run(self):
#         global item
#         for i in range(100):
#             time.sleep(1)
#             item = random.randint(0, 256)
#             self.items.append(item)
#             print('Producer notify : item %d appended to list by %s' % (item, self.name))
#             self.event.set()
#             print('Producer notify : event set by %s' % self.name)
#             time.sleep(1)
#             self.event.clear()
#             print('Produce notify : event cleared by %s ' % self.name)
#             time.sleep(2)
#
# if __name__ == '__main__':
#     t1 = producer(items, event)
#     t2 = consumer(items, event)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()


