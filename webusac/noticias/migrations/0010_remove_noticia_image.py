# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 19:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0009_auto_20160226_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='image',
        ),
    ]
