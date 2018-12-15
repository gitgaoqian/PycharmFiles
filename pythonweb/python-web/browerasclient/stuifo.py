# -*- coding: utf-8 -*- 这句代码可以让解释器识别中文
import flask 
app = flask.Flask(__name__)
address={'gao':'handan','jiang':'fuyang','cheng':'shenyang'}#建立一个数据库


#建立服务器 进入登录界面,get方法
@app.route('/signin',methods=['GET'])
def signin():
     return flask.render_template('signin.html')
     
@app.route('/search',methods=['POST'])
def search():
    username=flask.request.form['username']
    passwd=flask.request.form['password']
    if username=='ubuntu'and passwd=='ubuntu':
        return flask.render_template('search.html')
    else:
        return 'error,please sign in again'
@app.route('/addr',methods=['POST'])
def addr():
    name=flask.request.form['searchname']#获取POST请求的参数"searchname"字典对象,这个参数在search.html中有体现
    return address[name]
@app.route('/add',methods=['GET'])    
def addtion():#建立一个加法的函数,需要在url后加上参数
    a=flask.request.args.get('a')#得到的数据是字符串形式
    b=flask.request.args.get('b')
    c=int(a)+int(b)
    c=str(c)
    return c 

if __name__ == '__main__': 
	app.run("127.0.0.1",8080)

