#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2023/5/5

from flask import url_for, render_template, request, flash, redirect
from flask_login import login_user, logout_user, login_required, current_user

from watchlist.models import User, Movie, Message
from watchlist import db, app


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if not current_user.is_authenticated:
            return redirect(url_for('index'))

        title = request.form.get('title')
        year = request.form.get('year')
        if not title or not year or len(year) != 4 or len(title) > 60:
            flash('Invalid input.')
            return redirect(url_for('index'))

        movie_ins = Movie(title=title, year=year)
        db.session.add(movie_ins)
        db.session.commit()
        flash('Item created.')
        return redirect(url_for('index'))

    movies = Movie.query.all()
    res = render_template('index.html', movies=movies)
    return res


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash('username and password can not be empty')
            return redirect(url_for('login'))

        user_ins = User.query.first()
        if username == user_ins.username and user_ins.validate_password(password):
            login_user(user_ins)
            flash('Login success')
            return redirect(url_for('index'))
        else:
            flash('Not correct username or password')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout success')
    return redirect(url_for('index'))


@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    user = current_user
    if request.method == 'POST':
        name = request.form.get('name')

        if not name or len(name) > 20:
            flash('Invalid name')
            return redirect(url_for('settings'))

        user.name = name
        db.session.commit()
        flash('Modify name suceess')
        return redirect(url_for('index'))

    return render_template('settings.html')


@app.route('/movie/edit/<int:movie_id>', methods=['GET', 'POST'])
@login_required
def edit(movie_id):
    movie_ins = Movie.query.get_or_404(movie_id)
    if request.method == 'POST':
        title = request.form.get('title')
        year = request.form.get('year')
        if not title or not year or len(year) != 4 or len(title) > 60:
            flash('Invalid input.')
            return redirect(url_for('edit', movie_id=movie_id))
        movie_ins.title = title
        movie_ins.year = year
        db.session.commit()
        flash('Item updated.')
        return redirect(url_for('index'))

    res = render_template('edit.html', movie=movie_ins)
    return res


@app.route('/movie/delete/<int:movie_id>', methods=['POST'])
@login_required
def delete(movie_id):
    movie_ins = Movie.query.get_or_404(movie_id)
    db.session.delete(movie_ins)
    db.session.commit()
    flash('Item deleted.')
    return redirect(url_for('index'))

@app.route('/message_board',methods=['GET','POST'])
def message_board():
    if request.method == 'POST':
        username = request.form.get('username')
        message = request.form.get('message')
        if not username or not message or len(username) > 20:
            flash('Invalid message.')
            return redirect(url_for('message_board'))

        message_ins = Message(username=username, message=message)
        db.session.add(message_ins)
        db.session.commit()
        flash('Message created.')
        return redirect(url_for('message_board'))

    messages = Message.query.all()
    return render_template('message_board.html',messages=messages)
