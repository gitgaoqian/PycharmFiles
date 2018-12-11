# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 20:41:36 2018

@author: ros
"""
import matplotlib.pyplot as plt
def main():
    Number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    CloudProTime = [12.31,12.03,12.87,12.55,14,12.95,12.34,12.55,12.55,13.7,12.19,14.04,
             11.57,11.52,11.71,10.29,12.12,12.07,12.17,12.17]
    LocalProTime = [23.953,27.087,16.576,30.436,27.369,17.199,30.318,24.447,25.413,25.825,
                    24.293,25.405,25.562,24.991,23.007,22.562,22.399,21.564,20.386,21.584]
    [x,y]=[Number,CloudProTime]
    plt.figure()
    plt.plot(x,y,color='b', linewidth=1.5, linestyle='--',label='CLoudExeTime')
    [x,y]=[Number,LocalProTime]
    plt.plot(x,y,color='r', linewidth=1.5, linestyle='--', label='LocalExeTime')
    plt.xlabel('request times')
    plt.xlim(1,20)
    plt.ylabel('execute time (s)')
    plt.ylim((5, 35))
    plt.title("The Execute Time")
    plt.legend(loc='upper right')
   # plt.savefig('/home/ros/服务验证/time_task/protime.pdf')
    plt.show()

if __name__ == '__main__':
    main()
