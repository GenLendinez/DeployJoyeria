# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20171114_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reloj',
            name='imagen',
            field=models.ImageField(default='productos/default.jpg', height_field='150', help_text='Introducir imagen del producto[opcional]', upload_to='productos', width_field='150'),
        ),
    ]