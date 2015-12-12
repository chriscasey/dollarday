# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dd_app', '0005_auto_20151205_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='avg_earnings',
            field=models.FloatField(default=0, verbose_name=b'Avg $$$'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='score_dfm',
            field=models.FloatField(default=0, verbose_name=b'DFM'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='score_stddev',
            field=models.FloatField(default=0, verbose_name=b'SD'),
        ),
    ]
