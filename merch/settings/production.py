from .base import *

ROOT_URLCONF = 'merch.urls'

DEBUG = True
ALLOWED_HOSTS = ['ip-address', 'merch.com', 'merch.mn',
                 'ider0514.pythonanywhere.com', '127.0.0.1', '3.37.244.33']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 3,
        }},
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database',
        # 'NAME': '/opt/bitnami/projects/merch/db_name',
        'USER': 'super',
        'PASSWORD': 'merchstore',
        'HOST': '',
        'PORT': ''
    }
}
