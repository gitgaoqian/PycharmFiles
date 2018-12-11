# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 20:41:36 2018

@author: ros
"""
import matplotlib.pyplot as plt
def load_data(fileName):
    inFile = open(fileName, 'r')
    t=[]
    rate=[]
    num=1
    for line in inFile:
        t.append(num) #第一部分，即文件中的第一列数据逐一添加到list X 中
        rate.append(float(line.strip('\n'))) #第二部分，即文件中的第二列数据逐一添加到list y 中
        num=num+1
    return (t, rate)    # X,y组成一个元组，这样可以通过函数一次性返回  
def main():
    filename='/home/ros/image1.txt'
    [x,y]=load_data(filename)
    plt.figure()
    plt.plot(x,y,color='b', linewidth=1.5, linestyle='--',label='/camera/left/image_raw')
    filename='/home/ros/image1.txt'
    [x,y]=load_data(filename)
    plt.plot(x,y,color='r', linewidth=1.5, linestyle='--', label='/camera/scan')
    plt.xlabel('t')
    plt.xlim(0,175)
    plt.ylabel('rate')
    plt.ylim((0, 12))
    plt.title("The rate of topic")
    plt.legend(loc='upper right')
    plt.savefig(filename+'.pdf')
    plt.show()

if __name__ == '__main__':
    main()
