from flask import Flask

__author__ = 'mango'
app = Flask(__name__)

#@app.route('/hello')    #通过装饰器给hello函数 一个路由
def hello():
    #基于函数的试图（即插视图）
    return 'hello,mango~'

app.add_url_rule('/hello',view_func=hello)

app.run(debug=True)   #打开调试模式，不用每次手动重启
