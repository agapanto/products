# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20161109_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='local_code',
            field=models.CharField(default=123, max_length=40),
            preserve_default=False,
        ),
    ]
