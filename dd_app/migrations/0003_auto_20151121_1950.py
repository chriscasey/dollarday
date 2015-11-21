# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dd_app', '0002_entry_entry_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='avg_speed',
            field=models.FloatField(default=0),
        ),
    ]
