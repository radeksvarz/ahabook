# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahauser', '0002_ahauser_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='ahauser',
            name='remind_fr',
            field=models.BooleanField(verbose_name='Pá', default=True),
        ),
        migrations.AddField(
            model_name='ahauser',
            name='remind_mo',
            field=models.BooleanField(verbose_name='Po', default=True),
        ),
        migrations.AddField(
            model_name='ahauser',
            name='remind_sa',
            field=models.BooleanField(verbose_name='So', default=True),
        ),
        migrations.AddField(
            model_name='ahauser',
            name='remind_su',
            field=models.BooleanField(verbose_name='Ne', default=True),
        ),
        migrations.AddField(
            model_name='ahauser',
            name='remind_th',
            field=models.BooleanField(verbose_name='Čt', default=True),
        ),
        migrations.AddField(
            model_name='ahauser',
            name='remind_tu',
            field=models.BooleanField(verbose_name='Út', default=True),
        ),
        migrations.AddField(
            model_name='ahauser',
            name='remind_we',
            field=models.BooleanField(verbose_name='St', default=True),
        ),
    ]
