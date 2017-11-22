# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anillo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Introducir nombre representativo del anillo', max_length=100)),
                ('descripcion', models.CharField(blank=True, help_text='Introducir descripcion [opcional]', max_length=400)),
                ('precio', models.FloatField(help_text='Introducir precio del anillo', max_length=10)),
                ('diametro', models.IntegerField(help_text='Introducir diametro del anillo', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Cadena',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Introducir nombre representativo de la cadena', max_length=100)),
                ('descripcion', models.CharField(blank=True, help_text='Introducir descripcion [opcional]', max_length=400)),
                ('precio', models.FloatField(help_text='Introducir precio del cadena', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, help_text='Introducir fecha en la que se realizo la compra', null=True)),
                ('producto', models.IntegerField(help_text='Introducir id del producto (reloj,cadena ect..)')),
                ('tipo_producto', models.CharField(choices=[('r', 'Reloj'), ('c', 'Cadena'), ('a', 'Anillo')], default='r', help_text='Tipo producto', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Reloj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Introducir nombre representativo del reloj', max_length=100)),
                ('marca', models.CharField(help_text='Introducir marca del reloj', max_length=20)),
                ('descipcion', models.CharField(blank=True, help_text='Introducir descripcion [opcional]', max_length=400)),
                ('precio', models.FloatField(help_text='Introducir precio del reloj', max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Watch',
        ),
    ]
