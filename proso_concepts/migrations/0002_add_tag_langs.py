# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-07 10:04
from __future__ import unicode_literals

from django.db import migrations, models


def delete_tags(apps, schema_editor):
    Tag = apps.get_model("proso_concepts", "Tag")
    Tag.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('proso_concepts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='action',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='tag',
            name='lang',
            field=models.CharField(default='', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='type_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='value_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
                name='tag',
                unique_together=set([('type', 'value', 'lang')]),
        ),
        migrations.RunPython(delete_tags)   ,
    ]
