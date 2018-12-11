# -*- coding: utf-8 -*-
import threading  # 导入threading模块
import time  # 导入time模块

#--------------ex-1------------------------
class mythread(threading.Thread):  # 通过继承创建类
    def __init__(self, threadname):  # 初始化方法
        # 调用父类的初始化方法
        threading.Thread.__init__(self, name=threadname)

    def run(self):  # 重载run方法
        global x  # 使用global表明x为全局变量
        lock.acquire()
        for i in range(3):
            x = x + 1
        print (x)
        lock.release()


tl = []  # 定义列表
for i in range(10):
    t = mythread(str(i))  # 类实例化
    tl.append(t)  # 将类对象添加到列表中

x = 0  # 将x赋值为0
lock = threading.Lock()
for i in tl:
    i.start()  # 依次运行线程

#当不加锁时,输出全是30;枷锁之后,依次输出3,6,9..30,通过枷锁保证了同一时刻最多只有一个线程对共享资源进行操作.

# ----------------------------------ex-2------------------------------------------------
