INSTALLED_APPS = [
    # default Django apps...
    'rest_framework',  # ✅ Django REST Framework
    'api',             # ✅ Your app
]

# Use default SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
