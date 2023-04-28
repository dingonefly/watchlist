#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2023/4/15
import os
import sys
import click

from flask import Flask,url_for,render_template,request,flash,redirect
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
app.config['SECRET_KEY'] = 'dev'  # 等同于 app.secret_key = 'dev'

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

@app.context_processor
def inject_user():
    user = User.query.first()
    return dict(user=user)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        year = request.form.get('year')
        if not title or  not year or len(year) !=4 or len(title) >60:
            flash('Invalid input.')
            return redirect(url_for('index'))
        movie_ins = Movie(title=title,year=year)
        db.session.add(movie_ins)
        db.session.commit()
        flash('Item created.')
        return redirect(url_for('index'))

    movies = Movie.query.all()
    res = render_template('index.html',movies=movies)
    return res\

@app.route('/movie/edit/<int:movie_id>',methods=['GET','POST'])
def edit(movie_id):
    movie_ins = Movie.query.get_or_404(movie_id)
    if request.method == 'POST':
        title = request.form.get('title')
        year = request.form.get('year')
        if not title or  not year or len(year) !=4 or len(title) >60:
            flash('Invalid input.')
            return redirect(url_for('edit',movie_id=movie_id))
        movie_ins.title = title
        movie_ins.year = year
        db.session.commit()
        flash('Item updated.')
        return redirect(url_for('index'))

    res = render_template('edit.html',movie=movie_ins)
    return res

@app.route('/movie/delete/<int:movie_id>',methods=['POST'])
def delete(movie_id):
    movie_ins = Movie.query.get_or_404(movie_id)
    db.session.delete(movie_ins)
    db.session.commit()
    flash('Item deleted.')
    return redirect(url_for('index'))



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

@app.errorhandler(404)
def errorpage(e):
    user = User.query.first()
    return render_template('404.html',)
