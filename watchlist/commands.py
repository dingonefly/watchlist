#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2023/5/5
import click

from watchlist import db, app
from watchlist.models import User, Movie


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

    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)

    db.session.commit()
    click.echo('Done.')
@app.cli.command()
@click.option('--username',prompt=True,help='your name')
@click.option('--password',prompt=True,hide_input=True,confirmation_prompt=True,help='your password')
def admin(username,password):
    db.create_all()

    user = User.query.first()
    if user:
        click.echo('Update admin')
        user.usernaem = username
        user.set_password(password)
    else:
        click.echo('Create admin')
        user = User(name='Admin',username=username)
        user.set_password(password)
        db.session.add(user)

    db.session.commit()
    click.echo('Done.')
