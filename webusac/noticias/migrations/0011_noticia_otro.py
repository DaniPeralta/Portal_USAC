# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0010_remove_noticia_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='otro',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
