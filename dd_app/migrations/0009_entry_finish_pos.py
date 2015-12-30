# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dd_app', '0008_auto_20151221_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='finish_pos',
            field=models.IntegerField(default=0, verbose_name=b'Finish Position'),
        ),
    ]
