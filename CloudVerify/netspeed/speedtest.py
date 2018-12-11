# -*- coding: utf-8 -*-
'''
通过统计ifconfig命令的输出,计算当前网速
'''
#
# import logging
# logging.basicConfig(level=logging.INFO,
#                 format='%(message)s'
#                 )
engga
import os, sys, time
import re

def get_total_tx_bytes(interface, isCN):
    grep = '发送字节' if isCN else '"TX bytes"'
    r = os.popen('ifconfig '+interface+' | grep '+grep).read()
    total_bytes = re.sub('(.+:)| \(.+','',r)
    return int(total_bytes)

def get_total_rx_bytes(interface, isCN):
    grep = '接收字节' if isCN else '"RX bytes"'
    r = os.popen('ifconfig '+interface+' | grep '+grep).read()
    total_bytes = re.sub(' \(.+','',r)
    total_bytes = re.sub('.+?:','',total_bytes)
    return int(total_bytes)


if __name__=='__main__':    interface = 'wlan0' #定义接口
    Direction = 'tx' #获取发送流量还是接收流量
    Language = 'English' #ifconfig的显示是中文还是英文
    cycle = 1 #计算传输速率的周期
    isCN = True if Language == 'CN' else False
    get_total_bytes = get_total_tx_bytes if Direction == 'rx' else get_total_rx_bytes
    last = get_total_bytes(interface, isCN)
    print last
    while True:
        last = get_total_bytes(interface, isCN)
        time.sleep(cycle)
        delta = get_total_bytes(interface, isCN) - last
        speed = delta / cycle / 1000
        # logging.info(str(delta/cycle/1000))
