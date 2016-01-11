# inspired from https://github.com/arocks/edge/blob/master/src/project_name/settings/production.py
# In production set the environment variable like this:
#    DJANGO_SETTINGS_MODULE={{ project_name }}.settings.production

from .base import *             # NOQA
from os.path import join
import logging.config

# For security and performance reasons, DEBUG is turned off
DEBUG = False
# TEMPLATE_DEBUG = False

# Must mention ALLOWED_HOSTS in production!
ALLOWED_HOSTS = ["ahabook.cz", "ahabook.org", "ahabook-svarz.rhcloud.com"]

# Cache the templates in memory for speed-up
loaders = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]

TEMPLATES[0]['OPTIONS'].update({"loaders": loaders})
# TEMPLATES[0].update({"APP_DIRS": False})

# Define STATIC_ROOT for the collectstatic command
STATIC_ROOT = join(BASE_DIR, '..', 'site', 'static')


#TODO put to env vars!
RAVEN_CONFIG = {
    'dsn': 'https://97197e8d6d1b4309b83cf58ef457f76c:41f86676277e45609edb288507ce2995@app.getsentry.com/63207',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': release,
}


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
