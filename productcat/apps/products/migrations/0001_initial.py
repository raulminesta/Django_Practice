# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(verbose_name=datetime.datetime(2015, 11, 23, 22, 38, 54, 561797))),
            ],
            options={
                'db_table': 'manufacturers',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('created_at', models.DateTimeField(verbose_name=datetime.datetime(2015, 11, 23, 22, 38, 54, 562294))),
                ('manufacturer', models.ForeignKey(to='products.Manufacturer')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
