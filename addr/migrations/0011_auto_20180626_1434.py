# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-26 05:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('addr', '0010_auto_20180626_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='save_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 26, 5, 34, 56, 304929, tzinfo=utc)),
        ),
    ]
