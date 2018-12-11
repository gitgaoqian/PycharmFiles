# -*- coding: utf-8 -*-
a =[1,2,3,4, 5,6,4,5,7,8,9,0,23,4]
b=[]
for index, value in enumerate(a):
    if value == 4:
        b.append(index)
print b