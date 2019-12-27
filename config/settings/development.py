from .base import *
import socket

DEBUG = env('DEBUG', cast=bool)

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", "postgres"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "postgres"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}
INSTALLED_APPS += [
    'debug_toolbar',
    'djcelery_email'
]

EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'

MIDDLEWARE = [
                 'debug_toolbar.middleware.DebugToolbarMiddleware',
             ] + MIDDLEWARE

INTERNAL_IPS = [
    '127.0.0.1',
]

# Debugtoolbar for Docker
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS += [ip[:-1] + "1" for ip in ips]
