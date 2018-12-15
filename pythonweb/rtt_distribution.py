import  numpy as np
from scipy.stats import kstest
import matplotlib.pyplot as plt

f = open("/home/ros/ping.txt","r")
list = []
rtt = []
for line in f.readlines():
   result = line.strip("\n")
   list.append(result)
for index in list:
    result = float(index)
    rtt.append(result)

p = kstest(rtt,'norm')
bins = np.arange(1,30,0.5)
plt.hist(rtt,bins = bins)
plt.show()
