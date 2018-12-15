# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 20:28:50 2017

@author: ros
"""

import flask
app=flask.Flask(__name__)
@app.route('/file', methods=[ 'GET','POST'])
def upload():
    if flask.request.method=='GET':
        return '''
               <!DOCTYPE html>
               <html>
                   <body>
                       <h1>请选择一个文件上传</h1>
                       <form method='post'>
                       <input type='file' name='file' />
                       <input type='submit' value='上传'/>
                       </form>
                   </body>
                </html>
                '''
    else:
        file=flask.request.files['file']#获取上传对象
        if file:
            file.save(file.filename)
            return '上传成功'
if __name__=='__main__':
    app.run('127.0.0.1',8080)