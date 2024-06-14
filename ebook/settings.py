import os
from pathlib import Path
import environ
from dotenv import load_dotenv

# Initialize environment variables
env = environ.Env(
    DEBUG=(bool, True)
)

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
environ.Env.read_env(BASE_DIR / '.env')
load_dotenv(BASE_DIR / '.env')

# Security settings
DEBUG = env.bool('DEBUG')
SECRET_KEY = env('SECRET_KEY')

# Allowed hosts
ALLOWED_HOSTS = [
    'uniflex.onrender.com',
    'www.uniabujaflex.com.ng',
    'uniabujaflex.com.ng',
    'localhost',
    '127.0.0.1',
    '0.0.0.0',
    'uniflex-production.up.railway.app',
    'registry.npmjs.org',
    'uniflex-production-f9ea.up.railway.app'
]

# Application definition
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'library',
    'core',
    'location',
    'user',
    'site_analsys',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'site_analsys.middleware.VisitorTrackingMiddleware',
]

ROOT_URLCONF = 'ebook.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Static and Media URL/Root configurations
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Aliyun OSS settings
OSS_ACCESS_KEY_ID = env('OSS_ACCESS_KEY_ID')
OSS_ACCESS_KEY_SECRET = env('OSS_ACCESS_KEY_SECRET')
OSS_BUCKET_NAME = env('OSS_BUCKET_NAME')
OSS_ENDPOINT = env('OSS_ENDPOINT')

# Django storages settings for boto3
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_S3_REGION_NAME = 'us-west-1'
AWS_S3_ENDPOINT_URL = f'https://{OSS_ENDPOINT}'
AWS_ACCESS_KEY_ID = OSS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = OSS_ACCESS_KEY_SECRET
AWS_STORAGE_BUCKET_NAME = OSS_BUCKET_NAME

# Corrected Static and Media URLs
STATIC_URL = f'https://{OSS_BUCKET_NAME}.{OSS_ENDPOINT}/static/'
MEDIA_URL = f'https://{OSS_BUCKET_NAME}.{OSS_ENDPOINT}/media/'
AWS_S3_CUSTOM_DOMAIN = f'{OSS_BUCKET_NAME}.{OSS_ENDPOINT}'

# Security settings
# Uncomment these if you are using SSL
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

CSRF_TRUSTED_ORIGINS = [
    'https://www.uniabujaflex.com.ng',
    'https://uniabujaflex.com.ng',
    'https://uniflex.onrender.com',
    'https://uniflex-production.up.railway.app',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Lagos'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = "user:sign-in"
LOGOUT_REDIRECT_URL = "user:sign-in"
AUTH_USER_MODEL = 'user.User'

JAZZMIN_SETTINGS = {
    "site_header": "UniabujaFlex",
    "site_brand": "Learning Made Easy...",
    "copyright": "UniabujaFlex - All Rights Reserved © 2023",
}

JAZZMIN_UI_TWEAKS = {
    "theme": "cyborg",
    "dark_mode_theme": "cyborg",
}

WSGI_APPLICATION = 'ebook.wsgi.application'
