# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-03-13 02:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('username', models.CharField(max_length=50)),
                ('createtime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
        ),
    ]