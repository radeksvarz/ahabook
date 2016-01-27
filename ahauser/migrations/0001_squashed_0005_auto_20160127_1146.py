# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import timezone_field.fields


class Migration(migrations.Migration):

    replaces = [('ahauser', '0001_initial'), ('ahauser', '0002_auto_20160127_0143'), ('ahauser', '0003_auto_20160127_0144'), ('ahauser', '0004_ahauser_remind_hour'), ('ahauser', '0005_auto_20160127_1146')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AhaUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('email', models.EmailField(verbose_name='e-mailová adresa', db_index=True, unique=True, max_length=255)),
                ('gender', models.CharField(verbose_name='gender', choices=[('m', 'male'), ('f', 'female'), ('x', 'unknown')], default='x', max_length=1)),
                ('is_active', models.BooleanField(verbose_name='Aktivní', help_text='Určuje, zda bude uživatel považován za aktivního. Použijte tuto možnost místo odstranění účtů.', default=True)),
                ('is_admin', models.BooleanField(verbose_name='Admin', help_text='Určuje, zda se uživatel může přihlásit do správy tohoto webu.', default=False)),
                ('how_to_call', models.CharField(verbose_name='How to call you', blank=True, max_length=101)),
                ('timezone', timezone_field.fields.TimeZoneField(verbose_name='Timezone', default='Europe/Prague')),
                ('remind_hour', models.IntegerField(verbose_name='reminder hour', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24)], default=20)),
                ('date_joined', models.DateTimeField(verbose_name='datum registrace', default=django.utils.timezone.now)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
