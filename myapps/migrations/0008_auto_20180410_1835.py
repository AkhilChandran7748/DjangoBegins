# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-10 18:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0007_auto_20180410_1551'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='newBlogs',
            new_name='Blogs',
        ),
        migrations.RenameModel(
            old_name='User_registration',
            new_name='Users',
        ),
    ]
