INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'accounts',
    'posts',  # ✅ Add this line
]
INSTALLED_APPS = [
    ...
    'posts',
    'notifications',  # ✅ new app
]

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = False  # Must be False in production

ALLOWED_HOSTS = ['yourdomain.com', 'yourapp.herokuapp.com']  # Add your deployed domain

# Security settings
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True  # Only if using HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Database example for PostgreSQL (common in production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT', 5432),
    }
}

# Secret key should be stored in environment variable
SECRET_KEY = os.environ.get('SECRET_KEY')
