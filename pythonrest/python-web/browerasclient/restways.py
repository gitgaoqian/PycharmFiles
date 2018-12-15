# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, make_response,request
app = Flask(__name__)
articles = [
    {
        'id': 1,
        'title': 'the way to python',
        'content': 'tuple, list, dict'
    },
    {
        'id': 2,
        'title': 'the way to REST',
        'content': 'GET, POST, PUT'
    }
]
#get 方法
@app.route('/blog/api/articles', methods=['GET'])#定位资源,并限定了客户端访问的方法只能是GET
def get_articles():
    """ 获取所有文章列表 """
    return jsonify({'articles': articles[1]})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5632, debug=True)

