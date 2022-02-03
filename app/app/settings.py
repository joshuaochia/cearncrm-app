from pathlib import Path
import environ
import os

BASE_DIR = Path(__file__).resolve().parent.parent
BACKEND_TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
FRONTEND_TEMPLATE_DIR = os.path.join(BASE_DIR.parent, 'frontend', 'build')
print(FRONTEND_TEMPLATE_DIR)

env = environ.Env()
env_file = os.path.join(BASE_DIR.parent, ".env")

if os.path.isfile(env_file):
    env.read_env(env_file)
else:
    env.read_env(os.path.join(BASE_DIR.parent, '.env.dist'))

SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG')
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'leads'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BACKEND_TEMPLATE_DIR,FRONTEND_TEMPLATE_DIR],
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

WSGI_APPLICATION = 'app.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE": env.str("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": env.str("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": env.str("SQL_USER", "user"),
        "PASSWORD": env.str("SQL_PASSWORD", "password"),
        "HOST": env.str("SQL_HOST", "localhost"),
        "PORT": env.str("SQL_PORT", "5432"),
    }
}


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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'
BACKEND_STATIC_DIR = os.path.join(BASE_DIR, 'static')
FRONT_STATIC_DIR = os.path.join(BASE_DIR.parent, 'frontend', 'build', 'static')
STATICFILES_DIRS = [BACKEND_STATIC_DIR, FRONT_STATIC_DIR]

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#User Mode
AUTH_USER_MODEL = 'leads.User'
