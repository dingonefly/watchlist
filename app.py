#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2023/4/15
from flask import Flask
from flask import url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    msg = 'Welcome to my first flask project：WatchList'
    msg = '<h1>Welcome to my first flask project：WatchList</h1>' \
          '<img src="http://helloflask.com/totoro.gif">'
    return msg


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


