#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2023/4/15
from flask import Flask,url_for,render_template
from markupsafe import escape

app = Flask(__name__)

name = 'Yifei Ding'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]
@app.route('/')
def index():
    res = render_template('index.html',name=name,movies=movies)
    return res


@app.route('/user/<name>')
def userpage(name):
    msg = 'Welcome to my first flask project：WatchList'
    msg = f'<h5>{escape(name)}! Welcome to my first flask project：WatchList</h5>' \
          '<img src="http://helloflask.com/totoro.gif">'
    return msg

@app.route('/list_url')
def test_url_for():
    print(f'hello的url:{url_for("hello")}')
    print(f'userpage的url:{url_for("userpage",name="zhangsan")}')
    print(f'userpage的url:{url_for("userpage",name="lisi")}')
    print(f'test_url_for的url:{url_for("test_url_for")}')
    msg = {
        'hello': url_for("hello"),
        'userpage': url_for("userpage",name="zhangsan"),
        'test_url_for': url_for("test_url_for"),
    }

    return msg


