# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-26 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_auto_20160405_0310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='article',
        ),
        migrations.AlterField(
            model_name='ads',
            name='index',
            field=models.BooleanField(default=True, verbose_name='index'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='title',
            field=models.CharField(default='Titulo', max_length=50),
        ),
    ]