# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-06 11:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20180305_2051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='last_update',
            new_name='last_updated',
        ),
    ]