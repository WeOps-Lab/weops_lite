import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

ALLOWED_HOSTS = ['*']

# 基础组件
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_comment_migrate',
    'debug_toolbar',
    'import_export',
]

# Web组件
INSTALLED_APPS += [
    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'django_filters',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'auditlog',
]

# Celery
INSTALLED_APPS += [
    'django_celery_beat',
    'django_celery_results',
]

# 业务组件
INSTALLED_APPS += [
    'apps.core',
    'apps.system_mgmt'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'better_exceptions.integrations.django.BetterExceptionsMiddleware',
    'apps.core.middlewares.app_exception_middleware.AppExceptionMiddleware',
    'apps.core.middlewares.keycloak_auth_middleware.KeyCloakAuthMiddleware',

]

ROOT_URLCONF = 'weops_lite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'weops_lite.context_processors.web_env.custom_settings',  # 添加你的自定义上下文处理器
            ],
        },
    },
]

WSGI_APPLICATION = 'weops_lite.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True

STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = 'static/'

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = "/media/"

INTERNAL_IPS = ('127.0.0.1',)

WHITENOISE_ROOT = os.path.join(STATIC_ROOT)
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
