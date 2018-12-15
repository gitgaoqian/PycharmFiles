# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 08:21:55 2017

@author: ros
"""
import flask

app = flask.Flask(__name__)


@app.route('/register', methods=['POST'])
def register():
    
    print flask.request.form['name']
    print flask.request.form['password']
   
    return 'welcome'

if __name__ == '__main__':
    app.run('127.0.0.1',5566)