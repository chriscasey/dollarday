# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dd_app', '0003_auto_20151204_0555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='score_perc',
        ),
    ]
