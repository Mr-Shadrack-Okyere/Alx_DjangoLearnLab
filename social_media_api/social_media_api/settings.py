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
