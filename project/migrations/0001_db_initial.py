# -*- coding: utf-8 -*-
#
# Initial SQL setup of the PSQL DB for the project
#

from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        # allow unaccented search
        migrations.RunSQL('CREATE EXTENSION IF NOT EXISTS unaccent'),
        # enable DB level encryption
        migrations.RunSQL('CREATE EXTENSION IF NOT EXISTS pgcrypto'),
    ]
