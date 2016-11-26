# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-11-26 05:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proso_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('scheduled', models.DateTimeField()),
                ('processed', models.DateTimeField(auto_now=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'scheduled'), (1, 'sent'), (2, 'skipped'), (3, 'failed')])),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('html_message', models.TextField(blank=True, default=None, null=True)),
                ('from_email', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]