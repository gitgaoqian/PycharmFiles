#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:ros
import chardet
#读写一般的文本:要会read,readline,readlines,write,writelines,以及描述符号”r,rb,r+,w,wb,a,a+“等含义
# fr = open('read.txt','rb')#创建一个可以操作文件的对象
# fw = open("write.txt",'wb')
# for line in open('read.txt'):#此处不能写成“for line in f”,readline似乎不能用在二进制读取的文件对象
#     line = fr.readline()
#     print (line)
#     fw.write(line)
# fr.close()
# fw.close()#必须有close作为结尾

#读写图片文件，要明白这些文件内容的编码形式，文件读取的
# fr = open('meixi.jpg','rb')#创建一个可以操作文件的对象,而且必须使用二进制读的方式
# fw = open("meixi2.jpg",'wb')
# readBytes = fr.read()
# print (type(readBytes))
# print (chardet.detect(readBytes))
# fw.write(readBytes)
# fr.close()
# fw.close()#必须有close作为结尾

#读写音频文件,和图片的方式差不多,但是这里看不出来文件的 编码的方式.
fr = open('audio.wav','rb')#创建一个可以操作文件的对象,而且必须使用二进制读的方式,改二进制的编码方式是？
fw = open("audio2.wav",'wb')
readBytes = fr.read()
print (type(readBytes))
print (chardet.detect(readBytes))
# fw.write(readBytes)
fr.close()
fw.close()#必须有close作为结尾
