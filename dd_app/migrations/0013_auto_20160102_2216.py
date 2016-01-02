# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dd_app', '0012_auto_20160102_2204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='raceresult',
            old_name='lifetime_earning_exa_predicted',
            new_name='avg_earning_exa_predicted',
        ),
        migrations.RenameField(
            model_name='raceresult',
            old_name='lifetime_earning_sf_predicted',
            new_name='avg_earning_sf_predicted',
        ),
        migrations.RenameField(
            model_name='raceresult',
            old_name='lifetime_earning_tri_predicted',
            new_name='avg_earning_tri_predicted',
        ),
        migrations.RenameField(
            model_name='raceresult',
            old_name='lifetime_earning_win_predicted',
            new_name='avg_earning_win_predicted',
        ),
    ]
