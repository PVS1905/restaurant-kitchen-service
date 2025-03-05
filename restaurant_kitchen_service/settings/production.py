from .base import *


DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.environ["POSTGRES_DB_USER"],
        "PASSWORD": os.environ["POSTGRES_DB_PASSWORD"],
        "HOST": os.environ["POSTGRES_DB_HOST"],
        "PORT": int(os.environ["POSTGRES_DB_PORT"]),
    }
}
