# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 00:46:20 2016

@author: 程红太
"""
import os
import time

def swtichIP(newip):
    filename='/etc/network/interfaces'
    if newip=='':
        return False
    #加载当前配置文件，定位当前IP地址
    f = open(filename, 'r')
    fstr= f.read()
    f.close()
    head=fstr.find('address')+8
    tail=fstr.find('netmask')-1
    oldip=fstr[head:tail]
    #替换旧地址为新地址
    fstr=fstr.replace(oldip,newip)
    #写入新网卡配置文件
    f = open(filename, 'w')
    f.write(fstr)
    f.close()
    #执行系统更新命令
    os.system('sudo ifdown eth0')
    os.system('sudo ifup eth0')
    time.sleep(1)
    print 'IP has changed!'
    return True

