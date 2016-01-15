# -*- coding: utf-8 -*-
"""Local dev settings and globals.
"""

from .base import *
import raven

import environ

# env settings in env variable or env file
env = environ.Env(DEBUG=(bool, False), ) # set default values and casting
environ.Env.read_env(os.path.join(BASE_DIR, ".env")) # reading .env file

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(",")
print("Allowed hosts:%s" % ALLOWED_HOSTS)

# get the current git release version
RELEASE = raven.fetch_git_sha(BASE_DIR)[:8]
print ("Aha!book release: %s" % RELEASE)

########## DEBUG
DEBUG = True
print("Debug mode:%s" % DEBUG)

# depreceated - https://docs.djangoproject.com/en/1.8/ref/settings/#template-debug
# set by DEBUG - https://docs.djangoproject.com/en/1.8/topics/templates/#django.template.backends.django.DjangoTemplates
# TEMPLATE_DEBUG = DEBUG
# SERVE_MEDIA = DEBUG


INSTALLED_APPS += [
    'debug_toolbar',
]

# Database for dev - config from env var
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': env.db(), # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
}

debug_env_db = env.db()
debug_env_db["PASSWORD"] = "******"
print("DB:%s" % debug_env_db)

