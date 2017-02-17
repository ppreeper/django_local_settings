from .settings import *

DEBUG = True

# Local Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# StaticFiles
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
