# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-09 19:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0002_auto_20180409_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='newBlogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Blog_title', models.CharField(max_length=40)),
                ('Blog_content', models.CharField(max_length=150)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapps.User_registration')),
            ],
        ),
    ]
