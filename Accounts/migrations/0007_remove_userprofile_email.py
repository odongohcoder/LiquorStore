# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-23 21:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0006_userprofile_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
    ]
