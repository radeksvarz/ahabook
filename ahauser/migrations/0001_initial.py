# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid
import django.utils.timezone
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AhaUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('email', models.EmailField(verbose_name='e-mailová adresa', db_index=True, unique=True, max_length=255)),
                ('gender', models.CharField(verbose_name='gender', choices=[('m', 'male'), ('f', 'female'), ('x', 'unknown')], default='x', max_length=1)),
                ('how_to_call', models.CharField(verbose_name='How to call you', blank=True, max_length=101)),
                ('timezone', timezone_field.fields.TimeZoneField(verbose_name='Timezone', default='Europe/Prague')),
                ('remind_hour', models.IntegerField(verbose_name='reminder hour', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24)], default=20)),
                ('remind_mo', models.BooleanField(verbose_name='Po', default=True)),
                ('remind_tu', models.BooleanField(verbose_name='Út', default=True)),
                ('remind_we', models.BooleanField(verbose_name='St', default=True)),
                ('remind_th', models.BooleanField(verbose_name='Čt', default=True)),
                ('remind_fr', models.BooleanField(verbose_name='Pá', default=True)),
                ('remind_sa', models.BooleanField(verbose_name='So', default=True)),
                ('remind_su', models.BooleanField(verbose_name='Ne', default=True)),
                ('email_key', models.UUIDField(db_index=True, unique=True, default=uuid.uuid4)),
                ('is_admin', models.BooleanField(verbose_name='Admin', default=False, help_text='Určuje, zda se uživatel může přihlásit do správy tohoto webu.')),
                ('is_active', models.BooleanField(verbose_name='Aktivní', default=True, help_text='Určuje, zda bude uživatel považován za aktivního. Použijte tuto možnost místo odstranění účtů.')),
                ('date_joined', models.DateTimeField(verbose_name='datum registrace', default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(verbose_name='updated', auto_now=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
