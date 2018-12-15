# -*- coding: utf-8 -*- 这句代码可以让解释器识别中文
import flask 
import MySQLdb as mdb
app = flask.Flask(__name__)

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
def env_data():
    exo_id=flask.request.form['searchname']#获取POST请求的参数"searchname"字典对象,这个参数在search.html中有体现
    while 1:
        conn=mdb.connect(host="127.0.0.1",user="root",db="exo1213",passwd="ubuntu",charset="utf8")
        cur=conn.cursor(cursorclass=mdb.cursors.DictCursor)    
        cur.execute("select * from exo_table where id="+exo_id)
        result=cur.fetchall()
        atmo=result[0]["atmo"]
        temp=result[0]["temp"]
        hum=result[0]["hum"]
        return "atmo:"+str(atmo)+"  "+"temp:"+str(temp)+"  "+"hum:"+str(hum)
if __name__ == '__main__': 
    app.run("127.0.0.1",8080)

