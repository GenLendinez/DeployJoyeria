# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20171109_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anillo',
            name='diametro',
            field=models.IntegerField(help_text='Introducir diametro del anillo'),
        ),
    ]