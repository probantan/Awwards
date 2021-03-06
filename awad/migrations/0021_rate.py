# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-29 21:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awad', '0020_remove_project_landing_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.CharField(max_length=30)),
                ('usability', models.CharField(max_length=8)),
                ('creativity', models.CharField(blank=True, max_length=8, null=True)),
                ('average', models.FloatField(max_length=8)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rate', to='awad.Project')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
