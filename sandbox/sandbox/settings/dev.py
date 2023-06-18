from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-pij0uol#_6qhhdzt_y-=i(6i7$cd_4_7scc$2o&s*w))uc^x91"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

GDAL_LIBRARY_PATH = env.str('GDAL_LIBRARY_PATH', None)
GEOS_LIBRARY_PATH = env.str('GEOS_LIBRARY_PATH', None)

try:
    from .local import *
except ImportError:
    pass
