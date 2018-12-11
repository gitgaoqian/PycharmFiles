#!/usr/bin/env python
# coding: utf-8
'''
created in 2018-4-12
'''
import os
import time
class NetworkSim():
    def __init__(self):
        print "sim the dynamic network"
    def RttLimit(self,interface,delay,jitter):
        os.system("sudo tc qdisc replace dev " + interface + " root netem delay "+ delay +" "+jitter")
    def SpeedLimit(self,interface,speed):
        os.system("sudo wondershaper "+ interface + " " + speed + " " + speed)
if __name__ == "__main__":
    sim = NetworkSim()
    interface = "eth0"
    # 1-30s 保持高质量传输
    time.sleep(30)
    # 30-60s适当降低网络质量:
    sim.RttLimit(interface,30,10)
    sim.SpeedLimit(interface,2000)
    time.sleep(30)
    #继续降低
    sim.RttLimit(interface,50,10)
    sim.SpeedLimit(interface,1800)
    time.sleep(30)
    # 继续降低
    sim.RttLimit(interface, 80,20)
    sim.SpeedLimit(interface, 1500)