# watchlist
First Flask Project

tutorial: https://tutorial.helloflask.com/hello/

### 部署

1. 安装python3.8或者以上版本,安装Git
```commandline
yum install python38
python3 -V

yum install git
git -v
```
2. 克隆项目
```commandline
mkdir /home/xxx && cd /home/xxx/
git clone https://github.com/dingonefly/watchlist.git
```

3. 在项目根目录创建 .env 文件，写入
```commandline
cd /home/xxx/watchlist
vi .env

SECRET_KEY=3d6f45a5fc12445dbac2f59c3b6cxxxx  
DATABASE_FILE=data-prod.db
```

4. 新建虚拟环境
```commandline
cd /home/xxx/watchlist
$ python3 -m venv env  # 创建虚拟环境
$ . env/bin/activate  # 激活虚拟环境
(env) $ pip install -r requirements.txt  # 安装所有依赖
(env) $ flask initdb  # 初始化数据库
(env) $ flask admin  # 创建管理员账户 admin/admin123
```

5. 启动项目
Development
```commandline
(env) [root@xxx watchlist]#  flask run
 * Serving Flask app 'watchlist' (lazy loading)
 * Environment: development
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 205-802-684
```
或者
```commandline
(env) [root@xxx watchlist]#pip install gunicorn
gunicorn -b localhost:5000 -w 4 wsgi:app
```

Production
```commandline
(env) [root@xxx watchlist]#sed -i 's/xxx/{yourname}/g' ./deploykit/watchlist.service
cp ./deploykit/watchlist.service /etc/systemd/system/
systemctl daemon-reload

# 启动、查看、停止、重启
systemctl start watchlist.service
systemctl status watchlist.service
systemctl stop watchlist.service
systemctl restart watchlist.service
```

6. 项目更新
```commandline
$ cd watchlist
$ git pull
```