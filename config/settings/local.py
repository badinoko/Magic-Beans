import environ
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()
env.read_env(str(BASE_DIR / ".env"))

from .base import *  # noqa: F403
