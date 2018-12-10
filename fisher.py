from flask import Flask,make_response


__author__ = 'mango'
app = Flask(__name__)
app.config.from_object('config')

@app.route('/book/search')    #通过装饰器给hello函数 一个路由
def search():
    """
    q
    start
    count
    isbn

    """

    pass
def helloo():
    return 'hello,mango ...'

#app.run(host='0.0.0.0',debug=True,port=81)   #指定端口

if __name__ == '__main__':
    #生产环境 nginx + uwsgi
    app.run(host='0.0.0.0',debug=app.config['DEBUG'])   #1、指定ip（介绍外网的访问）；2、打开调试模式，不用每次手动重启
