# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
def load_data(fileName):
    inFile = open(fileName, 'r')
    x = np.arange(1,131,1)
    y = []
    for line in inFile:
        y.append(line.strip('\n')) #第二部分，即文件中的第二列数据逐一添加到list y 中
    return (x, y)    # x,y组成一个元组，这样可以通过函数一次性返回
def main():
    fig,netspeed = plt.subplots()
    # qos_score = netspeed.twinx()
    rtt = netspeed.twinx()

    file1 = 'netspeed.txt'
    [x,y1] = load_data(file1)
    lns1 = netspeed.plot(x,y1,color='r', linewidth=2.0, linestyle='-.',label='netspeed')
    netspeed.set_xlabel('request times')
    netspeed.set_ylabel('netspeed(KB/s)')


    file2 = 'rtt.txt'
    [x, y2] = load_data(file2)
    lns2 = rtt.plot(x,y2,color='g', linewidth=1.5, linestyle='-',label='rtt')
    rtt.set_ylabel('RTT(ms)   QoS_score')

    file3='qos_score.txt'
    [x,y3]=load_data(file3)
    lns3 = rtt.plot(x,y3,color='b', linewidth=2.0, linestyle='--',label='qos_score')

    #设置坐标轴刻度:
    rtt_yticks = np.linspace(0,120,25)
    rtt.set_yticks(rtt_yticks)
    netspeed_yticks = np.linspace(0,300,21)
    netspeed.set_yticks(netspeed_yticks)
    netspeed_xticks = np.linspace(0,130,14)
    netspeed.set_xticks(netspeed_xticks)

    #设置x的宽度
    plt.xlim(1,131)
    #设置标题
    plt.title('QoS Analysis')

    #合并图例
    lns = lns1 + lns2 + lns3
    labs = [l.get_label() for l in lns]
    plt.legend(lns, labs, loc='upper center')

    #划分qos_score的分界线
    plt.hlines(55, 1, 131, colors='k', linestyles='--')
    plt.hlines(60,1,131, colors='k', linestyles='--')
    plt.hlines(70, 1, 131, colors='k', linestyles='--')
    plt.hlines(85, 1, 131, colors='k', linestyles='--')
    plt.hlines(100, 1, 131, colors='k', linestyles='--')

    plt.savefig('/home/ros/qos.pdf')
    plt.show()

if __name__ == '__main__':
    main()
