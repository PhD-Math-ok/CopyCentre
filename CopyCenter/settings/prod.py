from .base import *

DEBUG = False




# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': env("POSTGRES_DB"),
    #     'USER': env("POSTGRES_USER"),
    #     'PASSWORD': env("POSTGRES_PASSWORD"),
    #     'HOST': env("POSTGRES_HOST"),
    #     'PORT': env("POSTGRES_PORT")
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('NAME'),
        'USER': "postgres",
        'PASSWORD': env('PASS_DB'),
        'HOST': env('HOST'),
    }
}