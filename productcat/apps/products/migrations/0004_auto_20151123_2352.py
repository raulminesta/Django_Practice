# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20151123_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 11, 23, 23, 52, 39, 80180)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 11, 23, 23, 52, 39, 80674)),
        ),
    ]
