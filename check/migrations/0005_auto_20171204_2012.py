# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-05 01:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0004_auto_20171203_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='letter_date1',
            field=models.BooleanField(default=False),
        ),
    ]