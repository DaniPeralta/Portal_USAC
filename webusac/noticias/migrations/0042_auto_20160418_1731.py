# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-18 23:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0041_auto_20160418_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos_beca',
            name='dpi',
            field=models.CharField(default=None, max_length=13, verbose_name='N\xba DPI'),
        ),
    ]
