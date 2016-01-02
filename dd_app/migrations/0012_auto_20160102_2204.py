# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dd_app', '0011_auto_20160102_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='RaceResultManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='raceresult',
            name='lifetime_earning_exa_predicted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='raceresult',
            name='lifetime_earning_sf_predicted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='raceresult',
            name='lifetime_earning_tri_predicted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='raceresult',
            name='lifetime_earning_win_predicted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='raceresult',
            name='win_perc_exa_predicted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='raceresult',
            name='win_perc_sf_predicted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='raceresult',
            name='win_perc_tri_predicted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='raceresult',
            name='win_perc_win_predicted',
            field=models.BooleanField(default=False),
        ),
    ]
