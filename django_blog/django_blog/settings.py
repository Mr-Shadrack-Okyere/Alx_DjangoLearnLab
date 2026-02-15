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
