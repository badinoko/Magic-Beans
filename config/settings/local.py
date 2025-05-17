import environ
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()
env.read_env(str(BASE_DIR / '.env'))

from .base import *  # noqa: F403

# Локальные настройки для разработки
DEBUG = True

ALLOWED_HOSTS = ['*']

# Пример для базы данных (если нужно переопределить)
DATABASES = {
    'default': env.db('DATABASE_URL', default='sqlite:///db.sqlite3')
}
