import os

from config.settings.common import *
from utils import get_database_config_variables

MIDDLEWARE = MIDDLEWARE + ["whitenoise.middleware.WhiteNoiseMiddleware"]

database_config_variables = get_database_config_variables(
    os.environ.get("DATABASE_URL")
)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": database_config_variables["DATABASE_NAME"],
        "HOST": database_config_variables["DATABASE_HOST"],
        "PORT": database_config_variables["DATABASE_PORT"],
        "USER": database_config_variables["DATABASE_USER"],
        "PASSWORD": database_config_variables["DATABASE_PASSWORD"],
    }
}

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
