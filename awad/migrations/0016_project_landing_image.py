# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-29 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awad', '0015_remove_project_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='landing_image',
            field=models.ImageField(null=True, upload_to='site-images/'),
        ),
    ]
