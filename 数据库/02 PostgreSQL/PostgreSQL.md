# 安装 PostgrsSQL

（1）配置镜像源

```shell
＃配置PostgreSQL官方源
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
#腾讯云镜像
sudo sh -c 'echo "deb https://mirrors.cloud.tencent.com/postgresql/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
#华为云镜像
sudo sh -c 'echo "deb https://mirrors.huaweicloud.com/postgresql/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
```

（2）导入签名密钥与安装

```shell
＃导入签名密钥：
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
＃更新软件包列表：
sudo apt-get update
＃安装PostgreSQL
sudo apt-get -y install postgresql libpq-dev
```

（3）查看数据库版本

```shell
psql --version
```

（4）允许远程连接

首先配置 `postgresql.conf`

```shell
$ find / -name "postgresql.conf"
/var/lib/pgsql/9.4/data/postgresql.conf
```

找到

```shell
listen_addresses = 'localhost'
```

换成：

```shell
listen_addresses = '*'
```

接着配置 `pg_hba.conf`：

在最后添加：

```shell

host    all             all              0.0.0.0/0                       md5
host    all             all              ::/0                            md5
```

参考博客：https://www.bigbinary.com/blog/configure-postgresql-to-allow-remote-connection

# 安装 pgAdmin4

（1）安装 key

```shell
sudo curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add
```

（2）配置镜像源：

```shell
# 配置pgAdmin官方源
sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
#腾讯云镜像
sudo sh -c 'echo "deb https://mirrors.cloud.tencent.com/postgresql/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
#华为云镜像
sudo sh -c 'echo "deb https://mirrors.huaweicloud.com/postgresql/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
```

（3）安装

```shell
# 安装pgAdmin4(桌面和web双模式)
sudo apt install pgadmin4

# 安装pgAdmin4-desktop(桌面单模式)
sudo apt install pgadmin4-desktop

# 安装pgAdmin4-web(web单模式)
sudo apt install pgadmin4-web 
# 如果已安装pgadmin4-web单模式，请运行以下命令:
sudo /usr/pgadmin4/bin/setup-web.sh
```

参考文章：https://www.huoxiaoqiang.com/basic/sql/3217.html

# PostgreSQL 常用命令

| 命令                                                         | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `sudo su - postgres`                                         | 切换到数据库用户                                             |
| `psql`                                                       | 登录 PostgreSQL 控制台                                       |
| `\password postgres`                                         | 为 postgres 用户设置一个密码                                 |
| `CREATE USER freeoadbuser WITH PASSWORD 'password';`         | 创建数据库用户freeoadbuser，并设置密码                       |
| `CREATE DATABASE freeoadb OWNER freeoadbuser;`               | 创建用户数据库，这里为freeoadb，并指定所有者为freeoadbuser   |
| `GRANT ALL PRIVILEGES ON DATABASE freeoadb to freeoadbuser;` | 将freeoadb数据库的所有权限都赋予freeoadbuser,否则freeoadbuser只能登录控制台，没有任何数据库操作权限 |
| `psql -U freeoadbuser -d freeoadb -h 127.0.0.1 -p 5432`      | 添加新用户和新数据库以后，以新用户的名义登录数据库，会提示输入密码 |
| `\l`                                                         | 列出所有数据库                                               |
| `\?`                                                         | 查看psql命令列表。                                           |
| `\c [database_name]`                                         | 使用指定数据库                                               |
| `\d`                                                         | 列出当前数据库的所有表格。                                   |
| `\d [table_name]`                                            | 列出某一张表格的结构                                         |
| `\du`                                                        | 列出所有用户                                                 |
| `\conninfo`                                                  | 列出当前数据库和连接的信息。                                 |

参考文章：http://www.freeoa.net/osuport/db/postgresql-comm-used-cmd-refer_3072.html

