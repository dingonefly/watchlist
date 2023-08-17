#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2023/8/17
# 是否开启debug模式
# debug = True
# 访问地址
bind = "0.0.0.0:5000"
# 工作进程数
workers = 4
# 工作线程数
# threads = 2
# 超时时间
timeout = 60
# 输出日志级别
loglevel = 'debug'
# 存放日志路径
pidfile = "./logs/gunicorn.pid"
# 存放日志路径
accesslog = "./logs/gunicorn_access.log"
# 存放日志路径
errorlog = "./logs/gunicorn_error.log"
# 是否以守护进程启动，默认false,将进程交给supervisor or systemctl管理
# daemon = 'false'
# 工作模式协程, gunicorn + apscheduler场景下，解决多worker运行定时任务重复执行的问题
worker_class = 'gevent'
# 设置最大并发量,默认 1000
# worker_connections = 1000
# preload_app = True

# 在加载应用程序之前切换目录；
# chdir=