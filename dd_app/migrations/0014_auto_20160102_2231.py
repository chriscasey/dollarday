# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dd_app', '0013_auto_20160102_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='raceresult',
            name='avg_speed_exa_predicted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='raceresult',
            name='avg_speed_sf_predicted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='raceresult',
            name='avg_speed_tri_predicted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='raceresult',
            name='avg_speed_win_predicted',
            field=models.BooleanField(default=False),
        ),
    ]
