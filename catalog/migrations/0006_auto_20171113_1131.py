# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20171110_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reloj',
            name='imagen',
            field=models.ImageField(default='media/productos/default.jpg', help_text='Introducir imagen del producto[opcional]', upload_to='media/productos'),
        ),
    ]
