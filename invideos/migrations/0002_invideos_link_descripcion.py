# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-30 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invideos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invideos',
            name='link_descripcion',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
