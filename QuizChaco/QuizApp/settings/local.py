from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'QuizApp',
        "USER": "postgres",
        "PASSWORD": 153624,
        "HOST":"127.0.0.1",
        "DATABASE_PORT":"5432"
    }
}