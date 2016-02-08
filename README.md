# ahabook
[![Requirements Status](https://requires.io/github/radeksvarz/ahabook/requirements.svg?branch=master)](https://requires.io/github/radeksvarz/ahabook/requirements/?branch=master)

 + autopopulate sites config in DB from settings (allows to have different sites for local development and production)

 + shows latest git commit release label in admin

 + shows environment label in admin (DEV / Production)

 + allauth integrated with Google and Linkedin SSO



Inspired from:
 -  A Django project skeleton that is modern and cutting edge. http://django-edge.readthedocs.org/ https://github.com/arocks/edge

 - A Cookiecutter template for creating production-ready Django projects quickly. https://github.com/pydanny/cookiecutter-django

 - Django OpenShift 1.8 https://github.com/Gpzim98/Django-OpenShift-1.8

 - Django OpenShift v2 https://github.com/jfmatth/openshift-django
    This git repository helps you get up and running quickly with django v1.7+ and Openshift.

Other:
 - justwriting photo by Joel Montes de Oca
 - used under license https://creativecommons.org/licenses/by-sa/2.0/


 SSO - Allauth (for social accounts)

 TODO - SAML 2
    - the project = Service Provider
    - ID servicces (Identity providers) - eg Okta, OneLogin, Pony Identity
    - check Sentry enterprise SSO

 Database related
    - unaccent search - https://www.odoo.com/forum/help-1/question/how-to-search-without-accented-characters-1229
    - enabled encryption on the DB level

    All setup via initial project migrations.

 FIXED: admin
  - bootstrapped - check boxes in horizontal
    - overriden fieldset template - see https://github.com/django-admin-bootstrapped/django-admin-bootstrapped/issues/191
