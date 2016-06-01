# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0019_auto_20160527_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='project',
        ),
        migrations.AddField(
            model_name='ticket',
            name='docfile',
            field=models.FileField(default=b'', upload_to=b'documents/%Y/%m/%d'),
        ),
    ]
