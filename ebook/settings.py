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
    # 'sslserver',
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
# Static and media files configuration
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Aliyun OSS settings
OSS_ACCESS_KEY_ID = os.getenv('OSS_ACCESS_KEY_ID')
OSS_ACCESS_KEY_SECRET = os.getenv('OSS_ACCESS_KEY_SECRET')
OSS_BUCKET_NAME = os.getenv('OSS_BUCKET_NAME')
OSS_ENDPOINT = os.getenv('OSS_ENDPOINT')

# Django storages settings for Aliyun OSS
DEFAULT_FILE_STORAGE = 'ebook.storages.AliyunOSSStorage'
STATICFILES_STORAGE = 'ebook.storages.AliyunOSSStorage'

# Static and Media URLs using virtual hosted style
ALIYUN_OSS_CUSTOM_DOMAIN = f'{OSS_BUCKET_NAME}.{OSS_ENDPOINT}'
STATIC_URL = f'https://{ALIYUN_OSS_CUSTOM_DOMAIN}/static/'
MEDIA_URL = f'https://{ALIYUN_OSS_CUSTOM_DOMAIN}/media/'

# Security settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False


CSRF_TRUSTED_ORIGINS = [
    'https://uniflex.onrender.com',
    'https://www.uniabujaflex.com.ng',
    'https://uniabujaflex.com.ng',
    'https://localhost',
    'https://127.0.0.1',
    'https://0.0.0.0',
    'https://uniflex-production.up.railway.app',
    'https://registry.npmjs.org',
    'https://uniflex-production-f9ea.up.railway.app'
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
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": "navbar-indigo",
    "accent": "accent-olive",
    "navbar": "navbar-indigo navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-indigo",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "cyborg",
    "dark_mode_theme": "cyborg",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    # New tweaks added below
    "sidebar_nav_icons": True,
    "sidebar_nav_flat": False,
    "sidebar_nav_legacy": False,
    "sidebar_nav_child_arrows": True,
    "sidebar_nav_labels": False,
    "sidebar_nav_indicators": True,
    "sidebar_nav_hover_expand": False,
    "sidebar_nav_light": False,
    "sidebar_nav_flat_hover": False,
    "sidebar_nav_legacy_hover": False,
    "sidebar_nav_child_indent_hover": False,
    "sidebar_nav_compact": False,
    "sidebar_nav_legacy_active": False,
    "sidebar_nav_legacy_fixed": False,
    "sidebar_nav_child_indent_active": False,
    "sidebar_nav_compact_hover": False,
    "sidebar_nav_legacy_hover_expand": False,
    "sidebar_nav_child_indent_hover_expand": False,
    "sidebar_nav_compact_hover_expand": False,
    "sidebar_nav_labels_hover_expand": False,
    "sidebar_nav_indicators_hover_expand": False,
    "sidebar_nav_active_bold": False,
    "sidebar_nav_active_italic": False,
    "sidebar_nav_active_light": False,
    "sidebar_nav_active_underline": False,
    "sidebar_nav_active_uppercase": False,
    "sidebar_nav_active_small_caps": False,
    "sidebar_nav_active_strikethrough": False,
    "sidebar_nav_active_text_sm": False,
    "sidebar_nav_active_text_xs": False,
    "sidebar_nav_active_text_xxs": False,
    "sidebar_nav_hover_bold": False,
    "sidebar_nav_hover_italic": False,
    "sidebar_nav_hover_light": False,
    "sidebar_nav_hover_underline": False,
    "sidebar_nav_hover_uppercase": False,
    "sidebar_nav_hover_small_caps": False,
    "sidebar_nav_hover_strikethrough": False,
    "sidebar_nav_hover_text_sm": False,
    "sidebar_nav_hover_text_xs": False,
    "sidebar_nav_hover_text_xxs": False,
    
        # New icon-related tweaks added below
    "sidebar_nav_icons": True,  # Enable sidebar navigation icons
    "sidebar_nav_icon_size": "sm",  # Set sidebar navigation icon size to small
    "sidebar_nav_icon_spacing": True,  # Add spacing between sidebar navigation icons and text
    "sidebar_nav_icon_color": "text-dark",  # Set sidebar navigation icon color to dark text color
    "sidebar_nav_icon_active_color": "text-primary",  # Set active sidebar navigation icon color to primary color

    # Additional icon tweaks for specific navigation items
    "sidebar_nav_icons_custom": {
        "dashboard": "fas fa-tachometer-alt",  # Custom icon for the dashboard navigation item
        "profile": "fas fa-user",  # Custom icon for the profile navigation item
        "settings": "fas fa-cog"
    }
}

WSGI_APPLICATION = 'ebook.wsgi.application'
