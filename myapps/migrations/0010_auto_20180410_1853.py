# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-10 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0009_auto_20180410_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='email',
            field=models.CharField(max_length=40),
        ),
    ]