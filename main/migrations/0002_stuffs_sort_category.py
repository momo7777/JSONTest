# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-18 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stuffs_sort',
            name='category',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
