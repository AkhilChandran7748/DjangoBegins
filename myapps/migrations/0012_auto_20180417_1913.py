# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-17 19:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0011_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='bid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='like',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
