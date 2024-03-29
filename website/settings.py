"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+*@z0@yd)t1p3suwsw28dbwq-7sbpv_$ez4o#j!#w(35k12m8#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'UserManage',
    'cm'
]

# 配置token验证机制
REST_FRAMEWORK = {
    # 权限认证
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',            # IsAuthenticated 仅通过认证的用户
        'rest_framework.permissions.AllowAny',                   # AllowAny 允许所有用户
        'rest_framework.permissions.IsAdminUser',                # IsAdminUser 仅管理员用户
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',  # IsAuthenticatedOrReadOnly 认证的用户可以完全操作，否则只能get读取
    ),
    # 身份认证
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',  # token认证
    )
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'website.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = ((os.path.join(BASE_DIR, 'static')), )

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 域控登录
# import ldap
# from django_auth_ldap.config import LDAPSearch
#
# AUTHENTICATION_BACKENDS = (
#     'django_auth_ldap.backend.LDAPBackend',
#     'django.contrib.auth.backends.ModelBackend',
# )
#
# '''测试域账号
# AUTH_LDAP_SERVER_URI = "ldap://192.168.186.81:389"
# AUTH_LDAP_BIND_DN = "CN=secadmin01,OU=secadmin,OU=sec,OU=99BILLTEST,DC=99billtest,DC=com"
# AUTH_LDAP_BIND_PASSWORD = "99bill.com"
# AUTH_LDAP_USER_SEARCH = LDAPSearch("DC=99billtest,DC=com",ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")
# '''
#
# AUTH_LDAP_SERVER_URI = "ldap://192.168.191.242:389"
# AUTH_LDAP_BIND_DN = "CN=sec_admin,OU=系统集成帐户,OU=99bill,DC=99bill,DC=com"
# AUTH_LDAP_BIND_PASSWORD = "8uhbCFT^"
# AUTH_LDAP_USER_SEARCH = LDAPSearch("DC=99bill,DC=com", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")
#
# # AD域如果是windows，必须加上这个选项
# AUTH_LDAP_CONNECTION_OPTIONS = {
#     ldap.OPT_DEBUG_LEVEL: 1,
#     ldap.OPT_REFERRALS: 0,
# }
#
# AUTH_LDAP_USER_ATTR_MAP = {
#     "username": "sAMAccountName",
#     "email": "userPrincipalName",
# }
#
# API_ACOUNT = {
#     'user':'SEC',
#     'pwd':'SEC@99bill.com'
# }

# 自定义用户表
AUTH_USER_MODEL = 'UserManage.User'


# 日志配置
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    'formatters': {  # 日志格式，提供给handler使用，非必须，如果不设置格式，默认只会打印消息体
        'verbose': {  # 格式名称
            # 2018-04-25 15:43:27,586 INFO views 8756 123145350217728 这是一个日志
            'format': '%(asctime)s [%(levelname)s] %(module)s %(message)s'
        },
        'simple': {
            # INFO  这是一个日志
            'format': '%(levelname)s %(message)s'
        },
        'standard': {
            # 2018-04-25 16:40:00,195 [Thread-7:123145575223296] [myapp.log:282] [views:user_query_json_get] [INFO]-
            # 这是一个日志
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'
        },
    },
    "handlers": {  # 日志处理方式，日志实例,向哪里输出
        "console": {  # 在控制台输出时的实例
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 使用的python的logging模块中的StreamHandler来进行输出
            'formatter': 'verbose'
        },
        'user_manage_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 日志位置,日志文件名,日志保存目录必须手动创建
            'filename': 'logs/user_manage.log',
            'maxBytes': 1024 * 1024 * 100,  # 日志文件的最大值,这里我们设置100M
            'backupCount': 10,
            'formatter': 'verbose',
        },
        'others_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/others.log',
            'maxBytes': 1024 * 1024 * 100,
            'backupCount': 30,
            'formatter': 'verbose',
        },
        'request_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/script.log',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 0,
            'formatter': 'verbose',
        },
        'scprits_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/script.log',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 0,
            'formatter': 'verbose',
        },

         'cm_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/cm.log',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 0,
            'formatter': 'verbose',
        },
        'test_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/test.log',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 0,
            'formatter': 'verbose',
        },


    },
    "loggers": {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'scripts': {
            'handlers': ['scprits_handler'],
            'level': 'INFO',
            'propagate': False
        },
        "django_auth_ldap": {
            "level": "DEBUG",
            "handlers": ["console"]
        },
        'user_manage': {
            'handlers': ['user_manage_handler'],
            'level': 'INFO',
            'propagate': False
        },
        'others': {
            'handlers': ['others_handler'],
            'level': 'INFO',
            'propagate': False
        },

         'cm': {
            'handlers': ['cm_handler'],
            'level': 'INFO',
            'propagate': False
        },

          'test': {
            'handlers': ['test_handler'],
            'level': 'INFO',
            'propagate': False
        },




    },
}
