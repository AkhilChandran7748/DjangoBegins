# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-09 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0004_auto_20180409_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newblogs',
            name='email',
            field=models.CharField(max_length=40),
        ),
    ]
