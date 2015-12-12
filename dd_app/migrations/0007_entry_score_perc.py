# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dd_app', '0006_auto_20151208_0204'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='score_perc',
            field=models.FloatField(default=0, verbose_name=b'Score %'),
        ),
    ]
