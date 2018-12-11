# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:14:46 2017

@author: ubuntu
"""

import  threading

# 假定这是你银行的存款
balance = 0

def change_it(n):
    # 先存后取，结果应该是0
    global balance
    balance = balance + n
    balance = balance - n
    print balance

def run_thread(n):
    for i in range(20):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

