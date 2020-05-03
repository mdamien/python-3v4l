from .base_settings import *

INSTALLED_APPS = ['core'] + INSTALLED_APPS

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'core/static/')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'python3v4l',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}