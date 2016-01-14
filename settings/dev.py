# -*- coding: utf-8 -*-
"""Local dev settings and globals.
"""

from .base import *


########## DEBUG
DEBUG = True
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
