# WeOps-Lite

WeOps-Lite是WeOps的轻量化版本。

# 本地开发

```
virtualenv venv -p python3.10
source ./venv/bin/active
pip install -r ./requirements/requirements.txt
pip install -r ./requirements/requirements-test.txt
cp ./.env.example .env
```

# 组件选型

| 名称              | 项目地址                                        | 用途              |
|-----------------|---------------------------------------------|-----------------|
| wrapt           | https://github.com/GrahamDumpleton/wrapt    | 通用装饰器代理         |
| django-auditlog | https://github.com/jazzband/django-auditlog | Django 自动审计日志模块 |

# 环境变量

| 变量                         | 默认值   | 示例                                              | 备注                 |
|----------------------------|-------|-------------------------------------------------|--------------------|
| SECRET_KEY                 |       | weops-lite                                      | 密钥，用于加密和保护敏感信息     |
| DEBUG                      | False | True                                            | 是否开启调试模式           |
| DB_ENGINE                  |       | django.db.backends.sqlite3                      | 数据库引擎类型            |
| DB_NAME                    |       | mydatabase                                      | 数据库名称              |
| DB_USER                    |       | myuser                                          | 数据库用户名             |
| DB_PASSWORD                |       | mypassword                                      | 数据库密码              |
| DB_HOST                    |       | localhost                                       | 数据库主机              |
| DB_PORT                    |       | 5432                                            | 数据库端口              |
| ENABLE_CELERY              | False | False                                           | 是否启用Celery任务队列     |
| CELERY_BROKER_URL          |       | redis://localhost:6379                          | Celery任务队列的代理URL   |
| CELERY_RESULT_BACKEND      |       | redis://localhost:6379                          | Celery任务结果的后端存储URL |
| CELERY_BEAT_SCHEDULER      |       | django_celery_beat.schedulers:DatabaseScheduler | Celery的定时任务调度器     |
| KEYCLOAK_URL               |       |                                                 | KeyCloak地址         |
| KEYCLOAK_ADMIN_USERNAME    |       |                                                 | KeyCloak管理员用户名     |
| KEYCLOAK_ADMIN_PASSWORD    |       |                                                 | KeyCloak管理员密码      |
| KEYCLOAK_REALM             |       |                                                 | KeyCloak Realm     |
| KEYCLOAK_CLIENT_ID         |       |                                                 | KeyCloak客户端ID      |
| KEYCLOAK_CLIENT_SECRET_KEY |       |                                                 | KeyCloak Client 秘钥 |
| SALT_API_URL               |       |                                                 | Salt API URL       |
| SALT_API_USERNAME          |       |                                                 | SaltAPI 用户名        |
| SALT_API_PASSWORD          |       |                                                 | SaltAPI 密码         |

# 使用命令行创建用户

```
python ./manage.py create_keycloak_user --role_type admin --username admin --password xxxx --email admin@qq.com --lastname 管理员
python ./manage.py create_keycloak_user --username admin --password xxxx --email admin@qq.com --lastname 管理员
```