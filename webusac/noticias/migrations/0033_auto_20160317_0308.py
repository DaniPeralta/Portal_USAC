# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-17 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0032_auto_20160317_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos_beca',
            name='edad',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='datos_beca',
            name='n_carne',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='datos_beca',
            name='n_colegiado',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='datos_beca',
            name='n_hermanos',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='datos_beca',
            name='n_reg_personal',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
