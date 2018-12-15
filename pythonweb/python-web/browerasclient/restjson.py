# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 20:34:54 2017

@author: ros
"""

import flask 
app = flask.Flask(__name__)
address={'gao':'handan','jiang':'fuyang','cheng':'shenyang'}#建立一个数据库
@app.route('/additon')
def()