# settings.py

# Point to the custom user model
AUTH_USER_MODEL = 'bookshelf.CustomUser'

# Media settings (if using profile_photo)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# settings.py

# SECURITY CONFIGURATION
DEBUG = False  # Turn off in production

# Browser-side protections
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Secure cookies
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Optional: HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True  # Redirect all HTTP to HTTPS

# Media settings (if using profile photos)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Tell Django to trust the X-Forwarded-Proto header from the proxy
# This is needed when running behind a reverse proxy (e.g., Nginx, Heroku)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
