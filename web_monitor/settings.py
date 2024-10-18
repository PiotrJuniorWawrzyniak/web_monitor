# from pathlib import Path
# import os
# from django.core.management.utils import get_random_secret_key
#
# # Ścieżka bazowa projektu
# BASE_DIR = Path(__file__).resolve().parent.parent
#
# # Klucz sekretu
# SECRET_KEY = os.getenv('SECRET_KEY', get_random_secret_key())
#
# # Tryb debugowania
# DEBUG = True  # Możesz zmienić na os.getenv('DEBUG', 'True') == 'True'
#
# # Dopuszczone hosty
# ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')
#
# # Zainstalowane aplikacje
# INSTALLED_APPS = [
#     "django.contrib.admin",
#     "django.contrib.auth",
#     "django.contrib.contenttypes",
#     "django.contrib.sessions",
#     "django.contrib.messages",
#     "django.contrib.staticfiles",
#     "blog",  # Twoja aplikacja
#     "django_celery_beat",
# ]
#
# # Middleware
# MIDDLEWARE = [
#     "django.middleware.security.SecurityMiddleware",
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
# ]
#
# # Plik główny URL
# ROOT_URLCONF = "web_monitor.urls"
#
# # Szablony
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [
#             os.path.join(BASE_DIR, 'frontend/build'),  # Katalog z buildem Reacta
#             os.path.join(BASE_DIR, 'templates'),  # Katalog z szablonami Django
#         ],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
#
# # Aplikacja WSGI
# WSGI_APPLICATION = "web_monitor.wsgi.application"
#
# # Konfiguracja bazy danych
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": os.getenv('POSTGRES_DB', 'web_monitor_db'),
#         "USER": os.getenv('POSTGRES_USER', 'web_monitor_user'),
#         "PASSWORD": os.getenv('POSTGRES_PASSWORD', 'your_secure_password'),
#         "HOST": os.getenv('POSTGRES_HOST', 'db'),
#         "PORT": os.getenv('POSTGRES_PORT', '5432'),
#     }
# }
#
# # Walidacja haseł
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
#     },
# ]
#
# # Międzynarodowe ustawienia
# LANGUAGE_CODE = "pl-pl"
# TIME_ZONE = "Europe/Warsaw"
# USE_I18N = True
# USE_TZ = True
#
# # Pliki statyczne (CSS, JavaScript, Obrazy)
# STATIC_URL = "/static/"
#
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'frontend/build/static'),
#     os.path.join(BASE_DIR, 'frontend/build'),
# ]
#
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#
# # Konfiguracja wyszukiwaczy plików statycznych
# STATICFILES_FINDERS = [
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# ]
#
# # Konfiguracja Celery
# CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://redis:6379/0')
# CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'redis://redis:6379/0')
# CELERY_ACCEPT_CONTENT = ["json"]
# CELERY_TASK_SERIALIZER = "json"
# CELERY_RESULT_SERIALIZER = "json"
# CELERY_TIMEZONE = TIME_ZONE
#
# CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers.DatabaseScheduler"
#
# # Domyślny typ klucza głównego
# DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

from pathlib import Path
import os
from django.core.management.utils import get_random_secret_key

# Ścieżka bazowa projektu
BASE_DIR = Path(__file__).resolve().parent.parent

# Klucz sekretu
SECRET_KEY = os.getenv('SECRET_KEY', get_random_secret_key())

# Tryb debugowania
DEBUG = True  # Możesz zmienić na os.getenv('DEBUG', 'True') == 'True'

# Dopuszczone hosty
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

# Zainstalowane aplikacje
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog",  # Twoja aplikacja
    "django_celery_beat",
    "corsheaders",  # Dodana obsługa CORS
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # Dodane middleware CORS
]

# Plik główny URL
ROOT_URLCONF = "web_monitor.urls"

# Szablony
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'frontend/build'),  # Katalog z buildem Reacta
            os.path.join(BASE_DIR, 'templates'),  # Katalog z szablonami Django
        ],
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

# Aplikacja WSGI
WSGI_APPLICATION = "web_monitor.wsgi.application"

# Konfiguracja bazy danych
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv('POSTGRES_DB', 'web_monitor_db'),
        "USER": os.getenv('POSTGRES_USER', 'web_monitor_user'),
        "PASSWORD": os.getenv('POSTGRES_PASSWORD', 'your_secure_password'),
        "HOST": os.getenv('POSTGRES_HOST', 'db'),
        "PORT": os.getenv('POSTGRES_PORT', '5432'),
    }
}

# Walidacja haseł
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Międzynarodowe ustawienia
LANGUAGE_CODE = "pl-pl"
TIME_ZONE = "Europe/Warsaw"
USE_I18N = True
USE_TZ = True

# Pliki statyczne (CSS, JavaScript, Obrazy)
STATIC_URL = "/static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/build/static'),
    os.path.join(BASE_DIR, 'frontend/build'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Konfiguracja wyszukiwaczy plików statycznych
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Konfiguracja Celery
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://redis:6379/0')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'redis://redis:6379/0')
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = TIME_ZONE

CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers.DatabaseScheduler"

# CORS - zezwalamy na połączenia z frontendem
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# CSRF - zaufane pochodzenia (domeny)
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]

# Domyślny typ klucza głównego
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Bezpieczne ustawienia dla CSRF (opcjonalnie, gdy używasz HTTPS)
CSRF_COOKIE_SECURE = os.getenv('CSRF_COOKIE_SECURE', 'False') == 'True'
