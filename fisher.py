from flask import Flask,make_response
from helper import is_isbn_or_key
from yushu_book import YuShuBook
import json
from flask import jsonify

__author__ = 'mango'
app = Flask(__name__)
app.config.from_object('config')

@app.route('/book/search/<q>/<page>')    #通过装饰器给hello函数 一个路由
def search(q,page):
    #以下代码是用来判断q是isbn还是关键字
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
        #难点：路由（url）的设计
        #dict 序列化
        #API + JS(单页面，NG、VUE、React 前后端分离 SEO
        #TPS + 小程序 + webview
        #网站 多页面 ajax
        #对立
        # C GO
        #API
    return jsonify(result)
    # return json.dumps(result),200,{'content-type':'application/json'}

def helloo():
    return 'hello,mango ...'

#app.run(host='0.0.0.0',debug=True,port=81)   #指定端口

if __name__ == '__main__':
    #生产环境 nginx + uwsgi
    app.run(host='0.0.0.0',debug=app.config['DEBUG'])   #1、指定ip（介绍外网的访问）；2、打开调试模式，不用每次手动重启
