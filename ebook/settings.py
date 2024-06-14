import os
from pathlib import Path
from dotenv import load_dotenv
import environ

# Initialize environment variables
env = environ.Env(
    DEBUG=(bool, True)
)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = Path(__file__).resolve().parent.parent
# Reading .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Base directory


load_dotenv(os.path.join(BASE_DIR, '.env'))

# Security settings
DEBUG = env('DEBUG')
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
    'django.middleware.security.SecurityMiddleware',
    'site_analsys.middleware.VisitorTrackingMiddleware',
]

ROOT_URLCONF = 'ebook.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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
STATIC_URL = 'https://uniabujaflex.oss-us-west-1.aliyuncs.com/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = 'https://uniabujaflex.oss-us-west-1.aliyuncs.com/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# OSS settings
OSS_ACCESS_KEY_ID = 'LTAI5tCub24r8bcgejLVfLZf'
OSS_ACCESS_KEY_SECRET = 'UZDCPmE9PL7JIFg2q148T6agZitSdB'
OSS_BUCKET_NAME = 'uniabujaflex'
OSS_ENDPOINT = 'oss-us-west-1.aliyuncs.com'

# Django storages settings
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_REGION_NAME = 'oss-us-west-1'
AWS_S3_ENDPOINT_URL = 'https://' + OSS_ENDPOINT

# Use different paths for static and media files
AWS_STORAGE_BUCKET_NAME_STATIC = 'uniabujaflex'
AWS_STORAGE_BUCKET_NAME_MEDIA = 'uniabujaflex'

STATIC_URL = 'https://' + AWS_STORAGE_BUCKET_NAME_STATIC + '.' + OSS_ENDPOINT + '/static/'
MEDIA_URL = 'https://' + AWS_STORAGE_BUCKET_NAME_MEDIA + '.' + OSS_ENDPOINT + '/media/'

# Security settings
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https','http')
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

CSRF_TRUSTED_ORIGINS = [
    'https://www.uniabujaflex.com.ng',
    'https://uniabujaflex.com.ng',
    'https://uniflex.onrender.com',
    'https://uniflex-production.up.railway.app',
]

DEBUG = os.getenv('DEBUG') == 'True'
SECRET_KEY = os.getenv('SECRET_KEY')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
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
    "site_brand": "learning Made Easy...",
    "copyright": "UniabujaFlex - All RIght Reserverd © Copyright 2023",
}

JAZZMIN_UI_TWEAKS = {
    "theme": "cyborg",
    "dark_mode_theme": "cyborg",
}

WSGI_APPLICATION = 'ebook.wsgi.application'
