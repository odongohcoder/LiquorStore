# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-20 11:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0011_userprofile'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('Delhi', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='description',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
