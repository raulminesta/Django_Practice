# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('productcats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='This is a product', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 11, 24, 1, 37, 59, 268064)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 11, 24, 1, 37, 59, 268553)),
        ),
    ]
