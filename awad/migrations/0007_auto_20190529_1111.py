# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-29 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awad', '0006_auto_20190529_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='default.jpeg', upload_to='pictures/'),
        ),
    ]
