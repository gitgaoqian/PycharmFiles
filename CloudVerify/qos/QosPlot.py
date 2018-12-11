# -*- coding: utf-8 -*-
'''
updated at 2018-5-16
'''
import matplotlib.pyplot as plt
import numpy as np
class Plot():
    def __init__(self):
        self.record = []
        self.datalen = 71
        self.x = np.arange(1,self.datalen+1,1)
        self.com_path = "/home/ros/qos/604/unadjust/"
        self.netspeedfile = self.com_path+"/netspeed.txt"
        self.compressfile = self.com_path + "compress.txt"
        self.rttfile = self.com_path+"rtt.txt"
        self.rdstfile = self.com_path+"rdst.txt"
        self.QosScorefile = self.com_path+"qos_score.txt"
    def Loadfile(self,file):
        inFile = open(file, 'r')
        y = []
        for line in inFile:
            l = float(line.strip("\n"))
            y.append(l) #导出文件的数据到列表
        return y    # X,y组成一个元组，这样可以通过函数一次性返回
    def PlotNetspeed(self):
        y = self.Loadfile(self.netspeedfile)
        plt.figure()
        plt.plot(self.x, y, color='b', linewidth=2, linestyle='--', label='rdst')
        plt.xlabel('Request times')
        plt.xlim(1, self.datalen)
        plt.ylabel('Netspeed')
        plt.ylim((0, 350))
        plt.savefig(self.com_path+'figure/netspeed.eps', format="eps")
        plt.savefig(self.com_path+'figure/netspeed.pdf', format="pdf")
        plt.show()
    def PlotCompress(self):
        y = self.Loadfile(self.compressfile)
        plt.figure()
        plt.plot(self.x, y, color='b', linewidth=2, linestyle='--', label='rdst')
        plt.xlabel('Request times')
        plt.xlim(1, self.datalen)
        plt.ylabel('compress')
        plt.ylim((0,100))
        plt.savefig(self.com_path+'figure/compress.eps',format="eps")
        plt.savefig(self.com_path+'figure/compress.pdf',format="pdf")
        plt.show()
    def PlotRTT(self):
        y = self.Loadfile(self.rttfile)
        plt.figure()
        plt.plot(self.x,y,color='b', linewidth=2, linestyle='--',label='RTT')
        plt.xlabel('Request times')
        plt.xlim(1,self.datalen)
        plt.ylabel('RTT (ms)')
        plt.ylim((0, 110))
        # plt.title("The rate of topic")
        # plt.legend(loc='RTT')
        # plt.savefig('/home/ros/服务验证/hz_topic/'+filename+'.pdf')
        #设置坐标轴刻度
        # y_tick = np.arange(0,100,10)
        # plt.yticks(y_tick)
        #画上Tg Tb线
        plt.hlines(10, 1, self.datalen, colors='r', linewidth=1.5, linestyles='--',label='Tg')
        plt.hlines(100, 1, self.datalen, colors='r', linewidth=1.5, linestyles='--', label='Tb')
        #添加注释
        plt.text(1.5, 10.5, 'Tg=10')
        plt.text(1.5, 100.5, 'Tb=100')
        #保存图片
        plt.savefig(self.com_path+'rtt.eps',format="eps")
        plt.savefig(self.com_path+'rtt.pdf', format="pdf")
        plt.show()
    def PlotNetwork(self):
        fig, netspeed = plt.subplots()
        rtt = netspeed.twinx()
        y1= self.Loadfile(self.netspeedfile)
        lns1 = netspeed.plot(self.x, y1, color='b', linewidth=2.5, linestyle='-.', label='netspeed')
        netspeed.set_xlabel('monitoring times')
        netspeed.set_ylabel('netspeed(KB/s)')

        y2 = self.Loadfile(self.rttfile)
        lns2 = rtt.plot(self.x, y2, color='b', linewidth=2, linestyle='--', label='rtt')
        rtt.set_ylabel('RTT(ms)')

        #画上Tg Tb线
        plt.hlines(10, 1, self.datalen, colors='r', linewidth=2, linestyles='--',label='Tg')
        plt.hlines(100, 1, self.datalen, colors='r', linewidth=2, linestyles='--', label='Tb')
        #添加注释
        plt.text(1.5, 10.5, 'Tg=10')
        plt.text(1.5, 100.5, 'Tb=100')

        # 合并图例
        lns = lns1 + lns2
        labs = [l.get_label() for l in lns]
        plt.legend(lns, labs, loc=1)
        # 设置x的宽度
        plt.xlim(1, self.datalen)
        # 设置坐标轴刻度:
        rtt_yticks = np.linspace(0, 120, 7)
        rtt.set_yticks(rtt_yticks)
        # #标记QoS改变的转折点
        # for i in self.record:
        #     plt.scatter([i+1, ], [y2[i], ], s=20, color='r')
        plt.savefig(self.com_path+'figure/network.eps', format="eps")
        plt.savefig(self.com_path+'figure/network.pdf', format="pdf")
        plt.show()
    def Plotrdst(self):
        y = self.Loadfile(self.rdstfile)
        # x1=[40,41]
        # y1=[5.2082,0]
        # x2 = range(42,57,1)
        # y2 = []
        # for i in range(len(x2)):
        #     y2.append(0.01)
        plt.figure()
        plt.plot(self.x, y, color='b', linewidth=2, linestyle='--', label='rdst')
        # # 增加画出当不采取措施时，rdst的变化趋势
        # plt.plot(x1, y1, color='r', linewidth=2, linestyle='--')
        # plt.plot(x2, y2, color='r', linewidth=2, linestyle='--')
        # plt.xlabel('Request times')
        # plt.xlim(1, self.datalen)
        # plt.ylabel('rdst')
        # plt.ylim((0, 11))
        # 设置x的宽度
        plt.xlim(1, self.datalen)
        #帧率理想线
        plt.hlines(9, 1, self.datalen, colors='r', linewidth=1.5, linestyles='--', label='rb')
        #帧率的基准线
        plt.hlines(6, 1, self.datalen, colors='r', linewidth=1.5, linestyles='--', label='rb')
        # 添加注释
        plt.text(2.5, 9.1, 'rate=9')
        plt.text(2.5, 6.1, 'rate=6')
        # plt.text(1.5, 90.5, 'Tb=90')
        #标记转折点
        for i in self.record:
            plt.scatter([i + 1, ], [y[i], ], s=20, color='r')
        plt.savefig(self.com_path+'figure/rdst.eps',format="eps")
        plt.savefig(self.com_path+'figure/rdst.pdf', format="pdf")
        plt.show()
    def PlotQosScore(self):
        y = self.Loadfile(self.QosScorefile)
        plt.figure(figsize=(15,10))
        plt.plot(self.x, y, color='b', linewidth=2, linestyle='--', label='Q')
        plt.xlabel('Request times')
        plt.xlim(1, self.datalen)
        plt.ylabel('Q')
        plt.ylim((0, 100))
        # 设置坐标轴刻度
        y_tick = np.arange(0,100,20)
        plt.yticks(y_tick)
        #Qos分界线
        plt.hlines(40, 1, self.datalen, colors='k', linestyles='--')
        plt.hlines(60, 1, self.datalen, colors='k', linestyles='--')
        plt.hlines(80, 1, self.datalen, colors='k', linestyles='--')
        #添加注释
        plt.text(3, 80.2, 'Q=80')
        plt.text(3, 60.2, 'Q=60')
        plt.text(3, 40.2, 'Q=40')
        #标记QoS改变的转折点
        self.record = self.QTurnPoint(y)
        print self.record
        for i in self.record:
            plt.scatter([i+1, ], [y[i], ], s=20, color='r')
        plt.savefig(self.com_path+'figure/qosscore.eps',format="eps")
        plt.savefig(self.com_path+'figure/qosscore.pdf', format="pdf")
        plt.show()
    def QTurnPoint(self,y):
        record = []
        lastQ = y[0]
        for i in range(self.datalen):
            curQ = y[i]
            lastQL = self.QosLevel(lastQ)
            curQL = self.QosLevel(curQ)
            if curQL != lastQL:
                record.append(i)
            lastQ = curQ
        return record
    def QosLevel(self,qos_score):
        qos_level = 1
        if 80 < qos_score < 100:
            qos_level = 1
        elif 60 < qos_score <= 80:
            qos_level = 2
        elif 40 < qos_score <= 60:
            qos_level = 3
        elif qos_score <= 40:
            qos_level = 4
        return qos_level
if __name__ == '__main__':
    p = Plot()
    p.PlotQosScore()  # Qos表述云服务质量的变化
    p.PlotNetwork()
    # p.PlotNetspeed()
    # p.PlotRTT()#RTT大致反映网络条件
    p.Plotrdst()#最显著的影响
    # p.PlotCompress()#改变的措施