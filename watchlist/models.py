#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2023/5/5
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from watchlist import db


class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    username =db.Column(db.String(20))
    password_hash = db.Column(db.String(128))

    def set_password(self,password):
        self.password_hash = generate_password_hash(password=password)

    def validate_password(self,password):
        return check_password_hash(self.password_hash,password)



class Movie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =db.Column(db.String(20))
    message = db.Column(db.Text)
    create_time = db.Column(db.DateTime,default=datetime.now, comment='插数据结果：每条记录创建的当前时间')