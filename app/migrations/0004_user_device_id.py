# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170924_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='device_id',
            field=models.BigIntegerField(default=0, unique=True),
        ),
    ]