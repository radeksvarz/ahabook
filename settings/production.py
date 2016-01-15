# inspired from https://github.com/arocks/edge/blob/master/src/project_name/settings/production.py
# In production set the environment variable like this:
#    DJANGO_SETTINGS_MODULE={{ project_name }}.settings.production

from .base import *             # NOQA
from os.path import join
import os
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

if 'OPENSHIFT_POSTGRESQL_DB_HOST' in os.environ:
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
