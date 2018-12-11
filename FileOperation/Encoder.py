#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:ros
import chardet
bytes = "abcd".encode("utf-8")
print (type(bytes))
print (chardet.detect(bytes))#获取编码的格式

Bytes  = '中文'.encode("utf-8")
print (type(Bytes))
print (chardet.detect(Bytes))#获取编码的格式
