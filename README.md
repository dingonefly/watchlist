# watchlist
First Flask Project

tutorial: https://tutorial.helloflask.com/hello/

### 部署

1. 系统安装python3.8或者以上版本
2. 克隆项目
```commandline
cd /home/
git clone https://github.com/dingonefly/watchlist.git
```

3. 在项目根目录创建 .env 文件，写入
```commandline
cd /home/watchlist
vi .env

SECRET_KEY=3d6f45a5fc12445dbac2f59c3b6cxxxx  # 随机生成的uuid
DATABASE_FILE=data-prod.db
```

4. 新建虚拟环境
```commandline
cd /home/watchlist
$ python3 -m venv env  # 创建虚拟环境
$ . env/bin/activate  # 激活虚拟环境
(env) $ pip install -r requirements.txt  # 安装所有依赖
(env) $ flask initdb  # 初始化数据库
(env) $ flask admin  # 创建管理员账户
```

5. 启动项目
```commandline
gunicorn xxx
待完成
```