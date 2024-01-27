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

# 目录结构

## 整体框架

```
-- apps: Django APP
-- requirement: 应用的依赖包定义
-- static: 静态资源目录
-- support-files: 应用的开发支撑文件
-- templates: Django 默认模板文件
-- weops_lite:
   -- components: Django Setting模块
   -- celery.py: Celery配置入口
   -- settings.py: 应用Settings主入口
   -- urls.py: 应用urls主入口
   -- wsgi.py: WSGI主入口
```

## 应用

```
-- decorators: 装饰器
-- entities: 内部强类型对象交互的时候，类型定义在这
-- exceptions: 自定义异常类型
-- management: Django自定义命令
-- middlewares: Django自定义中间件
-- migrations: 数据库Migrate文件
-- models: Django ORM模型
-- serializers: DRF与前端交互的数据类型，负责数据定义与校验
-- filters: DRF Filters目录，过滤条件写在这
-- services: 负责处理具体的业务逻辑
-- tasks: Celery定时任务
-- tests: 单元测试
-- utils: 工具类
-- views: DRF视图类，与前端进行数据交互，负责前端的数据接收，
调用serializers数据校验，调用service完成具体的业务逻辑，自身不处理业务相关的逻辑
-- admin.py: Django Admin定义文件
-- apps.py: Django App默认文件
-- constants.py: 静态变量
-- urls.py: DRF路由定义，会被应用自动加载
```

> 调用过程： views-->serializers-->services

# 组件选型

| 名称                            | 项目地址                                                                                                  | 用途                     |
|-------------------------------|-------------------------------------------------------------------------------------------------------|------------------------|
| wrapt                         | https://github.com/GrahamDumpleton/wrapt                                                              | 通用装饰器代理                |
| django-auditlog               | https://github.com/jazzband/django-auditlog                                                           | Django 自动审计日志模块        |
| whitenoise                    | https://github.com/evansd/whitenoise                                                                  | 静态文件Serving库           |
| redis                         | https://github.com/redis/redis-py                                                                     | redis驱动                |
| psycopg2-binary               | https://github.com/psycopg/psycopg2                                                                   | Postgres驱动             |
| Django                        | https://github.com/django/django                                                                      | Django Web框架           |
| django-split-settings         | https://github.com/wemake-services/django-split-settings                                              | Django Settings 分离库    |
| python-dotenv                 | https://github.com/theskumar/python-dotenv                                                            | 环境变量管理库                |
| daphne                        | https://github.com/django/daphne                                                                      | ASGI Server            |
| better_exceptions             | https://github.com/Qix-/better-exceptions                                                             | 异常信息打印库                |
| tqdm                          | https://github.com/tqdm/tqdm                                                                          | 进度条打印库                 |
| django-comment-migrate        | https://github.com/starryrbs/django-comment-migrate                                                   | Django Model注释迁移库      |
| joblib                        | https://github.com/joblib/joblib                                                                      | 轻量级Pipeline库           |
| pandas                        | https://github.com/pandas-dev/pandas                                                                  | 数据分析库                  |
| pydantic                      | https://github.com/pydantic/pydantic                                                                  | Python强类型库             |
| singleton-decorator           | https://github.com/Kemaweyan/singleton_decorator                                                      | 单例装饰器                  |
| djangorestframework           | https://github.com/encode/django-rest-framework                                                       | Django Rest API库       |
| django-filter                 | https://github.com/carltongibson/django-filter                                                        | DRF过滤工具类               |
| djangorestframework_simplejwt | https://github.com/jazzband/djangorestframework-simplejwt                                             | DRF Jwt认证后端            |
| django-cors-headers           | https://github.com/adamchainz/django-cors-headers                                                     | Django跨域工具             |
| django-celery-beat            | https://github.com/celery/django-celery-beat                                                          | 定时任务                   |
| flower                        | https://github.com/mher/flower                                                                        | Celery监控               |
| django-celery-results         | https://github.com/celery/django-celery-results                                                       | Celery任务后端存储           |
| sqlalchemy                    | https://github.com/sqlalchemy/sqlalchemy                                                              | 数据库访问工具类               |
| requests                      | https://github.com/psf/requests                                                                       | HTTP请求工具类              |
| python-keycloak               | https://github.com/marcospereirampj/python-keycloak                                                   | Keycloak客户端            |
| pycryptodome                  | https://github.com/Legrandin/pycryptodome                                                             | 加密函数库                  |
| pytest-django                 | https://github.com/pytest-dev/pytest-django                                                           | Pytest Django插件        |
| django-debug-toolbar          | https://github.com/jazzband/django-debug-toolbar                                                      | Django Debug工具         |
| drf-yasg                      | https://github.com/axnsan12/drf-yasg                                                                  | DRF Swagger库           |
| opentelemetry-distro          | https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/opentelemetry-distro         | OpenTelemetry Provider |
| opentelemetry-exporter-otlp   | https://github.com/open-telemetry/opentelemetry-python/tree/main/exporter/opentelemetry-exporter-otlp | OTLP协议导出器              |
| behave                        | https://github.com/behave/behave                                                                      | BDD测试库                 |

# 环境变量

| 变量                           | 默认值   | 示例                                              | 备注                 |
|------------------------------|-------|-------------------------------------------------|--------------------|
| SECRET_KEY                   |       | weops-lite                                      | 密钥，用于加密和保护敏感信息     |
| DEBUG                        | False | True                                            | 是否开启调试模式           |
| DB_NAME                      |       | mydatabase                                      | 数据库名称              |
| DB_USER                      |       | myuser                                          | 数据库用户名             |
| DB_PASSWORD                  |       | mypassword                                      | 数据库密码              |
| DB_HOST                      |       | localhost                                       | 数据库主机              |
| DB_PORT                      |       | 5432                                            | 数据库端口              |
| ENABLE_CELERY                | False | False                                           | 是否启用Celery任务队列     |
| CELERY_BROKER_URL            |       | redis://localhost:6379                          | Celery任务队列的代理URL   |
| CELERY_RESULT_BACKEND        |       | redis://localhost:6379                          | Celery任务结果的后端存储URL |
| CELERY_BEAT_SCHEDULER        |       | django_celery_beat.schedulers:DatabaseScheduler | Celery的定时任务调度器     |
| KEYCLOAK_URL                 |       |                                                 | KeyCloak地址         |
| KEYCLOAK_ADMIN_USERNAME      |       |                                                 | KeyCloak管理员用户名     |
| KEYCLOAK_ADMIN_PASSWORD      |       |                                                 | KeyCloak管理员密码      |
| KEYCLOAK_REALM               |       |                                                 | KeyCloak Realm     |
| KEYCLOAK_CLIENT_ID           |       |                                                 | KeyCloak客户端ID      |
| KEYCLOAK_CLIENT_SECRET_KEY   |       |                                                 | KeyCloak Client 秘钥 |
| SALT_API_URL                 |       |                                                 | Salt API URL       |
| SALT_API_USERNAME            |       |                                                 | SaltAPI 用户名        |
| SALT_API_PASSWORD            |       |                                                 | SaltAPI 密码         |
| TEST_BASE_URL                |       |                                                 | BDD测试使用的BaseURL    |
| KEYCLOAK_TEST_ADMIN          |       |                                                 | 测试用的KeyCloak管理员账号  |
| KEYCLOAK_TEST_ADMIN_PASSWORD |       |                                                 | 测试用的KeyCloak管理员密码  |

# 使用命令行创建用户

```
python ./manage.py create_keycloak_user --role_type admin --username admin --password xxxx --email admin@qq.com --lastname 管理员
python ./manage.py create_keycloak_user --username admin --password xxxx --email admin@qq.com --lastname 管理员
```