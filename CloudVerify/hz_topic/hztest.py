# coding: utf-8
import os
import time
def TopicHzCheck():
    # hz = os.popen("python rostopic.py | grep average")
    # list = hz.read().strip("\n").split(" ")
    # rdst = float(list[2])
    # return rdst
    file = os.popen("python rostopic.py")
    while 1:
        hz = file.readline()
        #print hz
        if "rate" in hz:  # 确保能够读到第一个出现的rate数据
            file.read()  # 把剩余的内容读完,不然会报错
            list = hz.strip("\n").split(" ")
            rdst = float(list[2])
            break
        if not hz:  # 如果读完了,还没有rate信息
            rdst = 0
            break
    return rdst

if __name__ == "__main__":
    rdst= TopicHzCheck()
    print rdst