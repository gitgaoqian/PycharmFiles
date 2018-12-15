# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 19:43:50 2017

@author: ros
"""

import flask
html_txt= '''
               <!DOCTYPE html>
               <html>
                   <body>
                       <h1>收到get请求</h1>
                       <form method='post'>
                       <input type='text' name='name' placeholder='输入名字'/>
                       <input type='submit' value='发送请求'/>
                       </form>
                   </body>
                </html>
                '''
app=flask.Flask(__name__)
@app.route('/hello', methods=[ 'GET','POST'])
def hello():
      if flask.request.method=='GET':
           return html_txt
      else:
         name ='name'in flask.request.form and flask.request.form['name']
         if name:
             return '!' + name + '!'
    
     
if __name__=='__main__':
	app.run('127.0.0.1',8080)
