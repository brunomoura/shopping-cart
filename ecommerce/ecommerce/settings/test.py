from .base import *

DEBUG = True
DEBUG_TEMPLATE = True
ALLOWED_HOSTS = ['*', ]
INTERNAL_IPS = ('127.0.0.1',)
SECRET_KEY = 'secret'

DATABASES = {
    'default': config(
        'DATABASE_URL_TEST',
        default='sqlite:///{0}/{1}'.format(
            BASE_DIR.child('db'),
            'ecommerce.sqlite3'),
        cast=db_url),
}


