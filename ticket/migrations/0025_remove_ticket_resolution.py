# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 14:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0024_auto_20160602_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='resolution',
        ),
    ]
