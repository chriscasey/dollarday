# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dd_app', '0007_entry_score_perc'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='lifetime_firsts',
            field=models.IntegerField(default=0, verbose_name=b'Lifetime Firsts'),
        ),
        migrations.AddField(
            model_name='entry',
            name='lifetime_seconds',
            field=models.IntegerField(default=0, verbose_name=b'Lifetime Seconds'),
        ),
        migrations.AddField(
            model_name='entry',
            name='lifetime_starts',
            field=models.IntegerField(default=0, verbose_name=b'Lifetime Starts'),
        ),
        migrations.AddField(
            model_name='entry',
            name='lifetime_thirds',
            field=models.IntegerField(default=0, verbose_name=b'Lifetime Thirds'),
        ),
    ]
