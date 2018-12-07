# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-02 04:31
from __future__ import unicode_literals

from django.db import migrations, models
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0011_auto_20171211_2200'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlackUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('username', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=255)),
                ('last_seen', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]