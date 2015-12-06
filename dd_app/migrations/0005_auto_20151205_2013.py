# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dd_app', '0004_remove_entry_score_perc'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='score_dfm',
            field=models.FloatField(default=0, verbose_name=b'Distance from the Mean'),
        ),
        migrations.AddField(
            model_name='entry',
            name='score_stddev',
            field=models.FloatField(default=0, verbose_name=b'Standard Deviation'),
        ),
    ]
