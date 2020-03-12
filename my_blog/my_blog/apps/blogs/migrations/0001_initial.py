# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-03-11 13:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=200)),
                ('nickname', models.CharField(default='匿名', max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('created_time', models.CharField(default=django.utils.timezone.now, max_length=50)),
                ('comment_num', models.PositiveIntegerField(default=0, verbose_name='评论数')),
                ('avatar', models.ImageField(default='media/default.png', upload_to='media')),
            ],
        ),
    ]
