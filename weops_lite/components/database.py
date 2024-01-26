import os
from pathlib import Path

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DB_ENGINE = os.getenv('DB_ENGINE')
if DB_ENGINE == 'django.db.backends.sqlite3':
    DATABASES = {
        'default': {
            'ENGINE': DB_ENGINE,
            'NAME': Path(__file__).resolve().parent.parent / (os.getenv('DB_NAME') + '.sqlite3'),
        }
    }
else:
    if DB_ENGINE == 'django.db.backends.mysql':
        import pymysql

        pymysql.install_as_MySQLdb()

    DATABASES = {
        'default': {
            'ENGINE': DB_ENGINE,
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT'),
        }
    }
