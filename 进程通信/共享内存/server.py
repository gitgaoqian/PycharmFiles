#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:ros

#开辟1kB空间作为共享内存，并且在网里面不断写“msg+num”的数据
import mmap
import contextlib
import time

with open("test.dat", "w") as f:
    f.write('\x00' * 1024)#写入1kB的空间

with open('test.dat', 'r+') as f:
    with contextlib.closing(mmap.mmap(f.fileno(), 1024, access=mmap.ACCESS_WRITE)) as m:#设置共享内存
        for i in range(1, 10001):
            m.seek(0)#设置文件指针的位置,0表示开头,1表示当前位置,2表示末尾
            s = "msg " + str(i)
            s.rjust(1024, '\x00')
            m.write(s)
            m.flush()
            time.sleep(1)
