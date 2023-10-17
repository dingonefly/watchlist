## .flaskenv和.env文件的作用

.flaskenv 用来存储 Flask 命令行系统相关的公开环境变量；而 .env 则用来存储敏感数据，不应该提交进 Git 仓库，我们把文件名 .env 添加到 .gitignore 文件的结尾（新建一行）来让 Git 忽略它。