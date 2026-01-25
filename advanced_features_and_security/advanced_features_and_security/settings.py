INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'bookshelf',
]

AUTH_USER_MODEL = 'users.CustomUser'

# Optional security (can add later)
DEBUG = True
