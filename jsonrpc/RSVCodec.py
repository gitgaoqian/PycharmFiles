# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 00:46:20 2016

@author: 程红太
"""
import re


class RSVCodec:

    def __init__(self, pre_fix="[%d,", post_fix="]", mid_fix=";", wild_cards="[%x,%y,%a,%i]"):
        self.setparameters(pre_fix, post_fix, mid_fix, wild_cards)

    def setparameters(self, pre_fix="[", post_fix="]", mid_fix=",", wild_cards="[%x,%y,%a,%i]"):
        self.prefix=pre_fix
        self.postfix=post_fix
        self.midfix=mid_fix
        self.wildcards=wild_cards
        self.segments=wild_cards.split('%')

        if self.prefix.find('%d') > -1:
            self.startindex=1
        else:
            self.startindex=0

        self.pattern = re.compile(r"[-+]?\d+\.?\d{0,2}")
        all=re.findall(r'%[a-z]',wild_cards)
        self.mapping =range(0,len(all))
        for i in range(0,len(all)):
            if all[i] =="%x":
                self.mapping[i]= 0
            elif all[i] =="%y":
                self.mapping[i] = 1
            elif all[i] == "%a":
                self.mapping[i] = 2
            elif all[i] == "%s":
                self.mapping[i] = 3
            else:
                self.mapping[i] = 4

    def getparameters(self):
        return self.prefix, self.postfix, self.midfix, self.wildcards

    def encode(self,values):
        N=len(values)
        if self.startindex==1:
            finalstr = self.prefix % N
        else:
            finalstr = self.prefix

        for i in range(0,N):
            value=values[i]
            #如果一开始就是具体值，没有前导，则有所区别
            if self.wildcards[0]=='%':
                singlestr = ""
                startindex_w=0
            else:
                singlestr=self.segments[0]
                startindex_w = 1

            for j in range(startindex_w,len(self.segments)):
                segment=self.segments[j]
                if segment[0] == 'x':
                    singlestr = '%s%.2f%s'%(singlestr,value[0],segment[1:])
                elif segment[0] == 'y':
                    singlestr = '%s%.2f%s'%(singlestr, value[1],segment[1:])
                elif segment[0] == 'a':
                    singlestr = '%s%.2f%s'%(singlestr, value[2],segment[1:])
                elif segment[0] == 's':
                    singlestr = '%s%.2f%s'%(singlestr, value[3],segment[1:])
                else :
                    singlestr = '%s%d%s'%(singlestr, value[4],segment[1:])

            if i<(N-1):
                singlestr=singlestr+self.midfix
            finalstr=finalstr+singlestr
        finalstr=finalstr+self.postfix
        return finalstr

    def decode(self,str):
        match = self.pattern.findall(str)
        values=[]
        N=len(match)
        M=len(self.mapping)
        for i in range(self.startindex,N,M):
            value=[0,0,0,0,0]
            for j in range(0,M):
                if self.mapping[j] <4 :
                    value[self.mapping[j]]= float(match[i+j])
                else:
                    value[self.mapping[j]] = int(match[i + j])
            values.append(value)
        return values

if __name__ == "__main__":
    codec=RSVCodec()
    values=[[1,2,3,4,5],[6,7,8,9,10]]
    strs= codec.encode(values)
    print strs
    print codec.decode(strs)
    print codec.getparameters()