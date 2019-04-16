# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-01-10 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [(b'crm', '0013_profile_qb_valid'), (b'crm', '0014_auto_20190110_0630'), (b'crm', '0015_auto_20190110_0637')]

    dependencies = [
        ('crm', '0012_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='qb_valid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='qb_access_token',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='qb_refresh_token',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AddField(
            model_name='profile',
            name='qb_refresh_expires',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='qb_token_expires',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]