配置新网站
==================

## 需要的包:

* nginx
* python 3.6+
* virtualenv + pip
* Git

以Ubuntu为例:

```bash
sudo add-apt-repository ppa:fkrull/deadsnakes  # Ubuntu18.04不用
sudo apt install nginx git python3.7 python3.7-venv
```

## Nginx虚拟主机

* 参考nginx.template.conf
* 把SITENAME替换成所需的域名,例如staging.my-domain.com


## Systemd服务

* 参考gunicorn-upstart.template.conf
* 把SITENAME替换成所需的域名,例如staging.my-domain.com


## 文件夹结构
假设有用户账号,家目录为/home/username

    /home/username
    └── sites
        └── SITENAME
            ├── database
            ├── source
            ├── static
            └── virtualenv
