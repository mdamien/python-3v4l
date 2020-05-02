from .base_settings import *

INSTALLED_APPS = ['core'] + INSTALLED_APPS

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'core/static/')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')