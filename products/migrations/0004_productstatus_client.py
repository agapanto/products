# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-24 23:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20161024_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='productstatus',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Client'),
        ),
    ]
