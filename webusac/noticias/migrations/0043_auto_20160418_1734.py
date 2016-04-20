# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-18 23:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0042_auto_20160418_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos_beca',
            name='dpi',
            field=models.CharField(max_length=13, verbose_name='N\xba DPI'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='dpi',
            field=models.CharField(choices=[('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No')], default='Requerido', max_length=10, verbose_name='N\xba DPI'),
        ),
        migrations.AlterUniqueTogether(
            name='datos_beca',
            unique_together=set([('beca', 'dpi')]),
        ),
    ]
