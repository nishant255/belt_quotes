# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 19:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0007_auto_20170127_1157'),
    ]

    operations = [
        migrations.DeleteModel(
            name='fav_quotes',
        ),
    ]
