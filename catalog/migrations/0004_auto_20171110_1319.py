# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20171109_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pendiente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Introducir nombre representativo del pendiente', max_length=100)),
                ('descripcion', models.CharField(blank=True, help_text='Introducir descripcion [opcional]', max_length=400)),
                ('precio', models.FloatField(help_text='Introducir precio del pendiente', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='reloj',
            name='imagen',
            field=models.ImageField(default='static/images/productos/default.jpg', upload_to='static/images/productos'),
        ),
    ]