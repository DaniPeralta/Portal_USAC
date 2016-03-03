# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 23:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0018_auto_20160302_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Universidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='experiencia',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='noticias.Universidad'),
        ),
        migrations.AlterField(
            model_name='experiencia',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='noticias.Anho'),
        ),
    ]
