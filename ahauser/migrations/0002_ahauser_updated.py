# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahauser', '0001_squashed_0005_auto_20160127_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='ahauser',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='updated'),
        ),
    ]
