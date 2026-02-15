INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',  # <- Add this line
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_blog_db',       # your database name
        'USER': 'your_db_user',         # your PostgreSQL username
        'PASSWORD': 'your_db_password', # your PostgreSQL password
        'HOST': 'localhost',            # database host
        'PORT': '5432',                 # default PostgreSQL port
    }
}
# URL prefix for static files
STATIC_URL = '/static/'

# Static files location in your project
STATICFILES_DIRS = [
    BASE_DIR / "static",  # optional if you have project-level static files
]

# If you want to collect static files for production
STATIC_ROOT = BASE_DIR / "staticfiles"
