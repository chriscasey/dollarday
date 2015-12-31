# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dd_app', '0009_entry_finish_pos'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='lifetime_earnings',
            field=models.FloatField(default=0, verbose_name=b'Lifetime Earnings'),
        ),
    ]
