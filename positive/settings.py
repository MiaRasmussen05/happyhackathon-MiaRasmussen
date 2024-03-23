from pathlib import Path
import os
import dj_database_url
import cloudinary
import cloudinary_storage
if os.path.isfile("env.py"):
   import env


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-$pv=uurdvq76ixbvv38_0d0b@+qnqh($@_j&l)8^=3(wk#dixm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['8000-adrianskelt-happyhackat-3ru8g22ktk1.ws-eu110.gitpod.io', '8000-adrianskelt-happyhackat-t6ku3p4u6k3.ws-eu110.gitpod.io', '127.0.0.1', '0.0.0.0', 'localhost', '8000-adrianskelt-happyhackat-rzsjp8tua6v.ws-eu110.gitpod.io', '8000-adrianskelt-happyhackat-t6ku3p4u6k3.ws-eu110.gitpod.io, *.ws-eu110.gitpod.io']
ALLOWED_HOSTS = ['localhost', '8000-adrianskelt-happyhackat-3ru8g22ktk1.ws-eu110.gitpod.io', 'positive-note-ec9b8f1f6fb7.herokuapp.com', '8000-adrianskelt-happyhackat-ervvbwdq0eq.ws-eu110.gitpod.io']
CSRF_TRUSTED_ORIGINS = ['https://*.ws-eu110.gitpod.io','https://*.ws-eu110.gitpod.io', 'http://*.ws-eu110.gitpod.io','http://*.ws-eu110.gitpod.io', 'https://3001-adrianskelt-happyhackat-3ru8g22ktk1.ws-eu110.gitpod.io', 'https://3002-adrianskelt-happyhackat-3ru8g22ktk1.ws-eu110.gitpod.io',]

CORS_ORIGIN_ALLOW_ALL = True 

CORS_ALLOWED_ORIGINS = [
    'https://3001-adrianskelt-happyhackat-3ru8g22ktk1.ws-eu110.gitpod.io',
    'https://3002-adrianskelt-happyhackat-3ru8g22ktk1.ws-eu110.gitpod.io',
    'https://positive-note-ec9b8f1f6fb7.herokuapp.com',
    'https://localhost',
    'https://*.ws-eu110.gitpod.io'
]

# Application definition

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'affirmation',
    'profiles',
    'accounts',
    'corsheaders',
]

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware', #added this
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Added WhiteNoise middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'positive.urls'

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

WSGI_APPLICATION = 'positive.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}
#DATABASES = {
#     'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'zirpwyzo',                              
        'USER': 'zirpwyzo',                             
        'PASSWORD': 'TtcJ29g3Cqad2Larok9Yb85EVlrOLCM9',  
        'HOST': 'snuffleupagus.db.elephantsql.com',      
        'PORT': '5432',                                  
    }
}
X_FRAME_OPTIONS = 'SAMEORIGIN'  
SECRET_KEY = os.environ.get('SECRET_KEY')

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  
#STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dmtdimx2z',
    'API_KEY': '426283364777722',
    'API_SECRET': 'Y4zDYrA3X_0DA-7_yuxdBipkW3s',
}

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage' 

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  
