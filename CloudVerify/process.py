#!/usr/bin/env python
# coding: utf-8
'''
created in 2018-4-14
http://www.sijitao.net/2046.html
'''
import psutil as pt
class Process():
    def getNamebyPid(self,pid):
        pids = pt.Process(pid)
        return pids


    def getPidByName(self,str):
        pids = pt.process_iter()
        pidList = []
        for pid in pids:
            if pid.name() == name:
                pidList.append(pid.pid)
        return pidList

if __name__ == '__main__':
    process = Process()

    #pid = process.getPidByName('chrome.exe')
    pids = process.getNamebyPid(29540)
    print pids