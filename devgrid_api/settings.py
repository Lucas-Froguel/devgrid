"""
Django settings for devgrid_api project.

Generated using django-split-settings, dj-database-url and python-decouple
"""
from pathlib import Path
import decouple

BASE_DIR = Path(__file__).resolve().parent.parent

config = decouple.AutoConfig(BASE_DIR)

SECRET_KEY = config("DJANGO_SECRET_KEY")
DEBUG = config("DJANGO_DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config(
    "DJANGO_ALLOWED_HOSTS", cast=lambda v: [s.strip() for s in v.split(",")]
)

APPEND_SLASH = True

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "health_check",
    "rest_framework",
    "devgrid_api",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "devgrid_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "devgrid_api.wsgi.application"

LANGUAGE_CODE = "en"
TIME_ZONE = "UTC"
USE_I18N = False
USE_TZ = False

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"
STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = STATIC_ROOT / "media"

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "EXCEPTION_HANDLER": "devgrid_api.utils.custom_exception_handler.custom_exception_handler",
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {"anon": "10/minute", "user": "1000/minute"},
    "COERCE_DECIMAL_TO_STRING": False,
}


MONGO_DATABASE_URL = config("MONGO_DATABASE_URL")
MONGODB_NAME = config("MONGO_DATABASE")
MONGO_CITIES_DATA_COLLECTION=config("MONGO_CITIES_DATA_COLLECTION")
MONGO_USERS_COLLECTION=config("MONGO_USERS_COLLECTION")

OPEN_WEATHER_KEY = config("OPEN_WEATHER_KEY")
OPEN_WEATHER_URL = config("OPEN_WEATHER_URL")
