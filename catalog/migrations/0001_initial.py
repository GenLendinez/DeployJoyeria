# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Introducir titulo representativo del reloj', max_length=100)),
                ('brand', models.CharField(help_text='Introducir marca del reloj', max_length=20)),
            ],
        ),
    ]
