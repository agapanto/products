# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_productstatus_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.URLField(blank=True, max_length=255),
        ),
    ]
