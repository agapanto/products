# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-06 19:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_productinstance_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricetype',
            name='client',
        ),
        migrations.RemoveField(
            model_name='productinstance',
            name='client',
        ),
        migrations.RemoveField(
            model_name='productstatus',
            name='client',
        ),
    ]
