# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20151123_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='manufacturer',
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 11, 23, 23, 55, 26, 740726)),
        ),
        migrations.DeleteModel(
            name='Manufacturer',
        ),
    ]
