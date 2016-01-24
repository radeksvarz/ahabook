# inspired from https://github.com/arocks/edge/blob/master/src/project_name/settings/production.py
# In production set the environment variable like this:
#    DJANGO_SETTINGS_MODULE={{ project_name }}.settings.production

from .base import *             # NOQA
from os.path import join
import os

import environ

# env settings in env variable or env file
env = environ.Env(DEBUG=(bool, False), ) # set default values and casting
ENV_DIR = os.path.join(os.environ.get('OPENSHIFT_HOMEDIR'), '.env/user_vars')
environ.Env.read_env(os.path.join(ENV_DIR, ".env")) # reading .env file

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# For security and performance reasons, DEBUG to be turned off inproduction
DEBUG = env('DEBUG') # False if not in os.environ
# TEMPLATE_DEBUG = False # - deprecated
print("Debug mode:%s" % DEBUG)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# Must mention ALLOWED_HOSTS in production!
ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(",")
print("Allowed hosts:%s" % ALLOWED_HOSTS)

# get the current git release version - populated by CI
# RELEASE = env("RELEASE")
import raven
import six
def git_revision():
    head_path = os.path.join(os.environ.get('OPENSHIFT_HOMEDIR'), 'git/ahabook.git', 'HEAD')
    if not os.path.exists(head_path):
        return "n/a"

    with open(head_path, 'r') as fp:
        head = six.text_type(fp.read()).strip()

    if head.startswith('ref: '):
        revision_file = os.path.join(
            os.environ.get('OPENSHIFT_HOMEDIR'), 'git/ahabook.git', *head.rsplit(' ', 1)[-1].split('/')
        )
    else:
        return head

    with open(revision_file, 'r') as fh:
        return six.text_type(fh.read()).strip()

    return "n/a"


RELEASE = git_revision()[:8]

# We want to add site info automatically
SITES = [(1, "https://ahabook.cz", "Aha!book"),]

import logging.config


# Cache the templates in memory for speed-up
# Cannot use now:
#  error: app_dirs must not be set when loaders is defined
# loaders = [
#     ('django.template.loaders.cached.Loader', [
#         'django.template.loaders.filesystem.Loader',
#         'django.template.loaders.app_directories.Loader',
#     ]),
# ]
#
# TEMPLATES[0]['OPTIONS'].update({"loaders": loaders})
# TEMPLATES[0].update({"APP_DIRS": False})

# Define STATIC_ROOT for the collectstatic command
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
# We want to collect static files to the persistent data dir, so it is not deleted during Openshift git push deployment
# On Openshift it is symlinked to the ./repo/wsgi/static
# If using on local PC, the default project static dir is used
STATIC_ROOT = os.path.join(os.environ.get('OPENSHIFT_DATA_DIR'), 'static')

# old Openshift compatibility (static files are deleted during git push)
#if os.environ.has_key('OPENSHIFT_REPO_DIR'):
#    STATIC_ROOT = os.path.join(os.environ.get('OPENSHIFT_REPO_DIR'), 'wsgi', 'static')


RAVEN_CONFIG = {
    'dsn': env("SENTRY_DSN"),
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': RELEASE,
}

print ("Aha!book release: %s" % RELEASE)

print("Raven %s: " % env("SENTRY_DSN"))


# DB settings based on Openshift variables

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('OPENSHIFT_APP_NAME'),
        'USER': os.environ.get('OPENSHIFT_POSTGRESQL_DB_USERNAME'),
        'PASSWORD': os.environ.get('OPENSHIFT_POSTGRESQL_DB_PASSWORD'),
        'HOST': os.environ.get('OPENSHIFT_POSTGRESQL_DB_HOST'),
        'PORT': os.environ.get('OPENSHIFT_POSTGRESQL_DB_PORT'),
    }
}

ENV="PRODUCTION"

SETTINGS_EXPORT = [
    'ENV',
    'RELEASE',
]

# We use SENTRY for logging

# Log everything to the logs directory at the top
# LOGFILE_ROOT = join(dirname(BASE_DIR), 'logs')

# # Reset logging
# LOGGING_CONFIG = None
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': "[%(asctime)s] %(levelname)s [%(pathname)s:%(lineno)s] %(message)s",
#             'datefmt': "%d/%b/%Y %H:%M:%S"
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'handlers': {
#         'proj_log_file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': join(LOGFILE_ROOT, 'project.log'),
#             'formatter': 'verbose'
#         },
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         }
#     },
#     'loggers': {
#         'project': {
#             'handlers': ['proj_log_file'],
#             'level': 'DEBUG',
#         },
#     }
# }

# logging.config.dictConfig(LOGGING)
