#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2023/4/15
import os
import sys
import click

from flask import Flask,url_for,render_template
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqllite:////'

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控

db = SQLAlchemy(app)  # 初始化扩展，传入程序实例 app

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))

class Movie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))


@app.cli.command()
@click.option('--drop',is_flag = True,help='Create after drop.')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')

@app.cli.command()
def forge():
    """Generate fake data."""
    db.create_all()

    # 全局的两个变量移动到这个函数内
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

    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)

    db.session.commit()
    click.echo('Done.')

@app.route('/')
def index():
    user = User.query.first()
    movies = Movie.query.all()
    res = render_template('index.html',user=user,movies=movies)
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


