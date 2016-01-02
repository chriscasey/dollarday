# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dd_app', '0010_entry_lifetime_earnings'),
    ]

    operations = [
        migrations.CreateModel(
            name='RaceResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score_win_predicted', models.BooleanField(default=False)),
                ('score_exa_predicted', models.BooleanField(default=False)),
                ('score_tri_predicted', models.BooleanField(default=False)),
                ('score_sf_predicted', models.BooleanField(default=False)),
                ('race', models.ForeignKey(to='dd_app.Race')),
            ],
        ),
        migrations.AlterField(
            model_name='entry',
            name='avg_earnings',
            field=models.FloatField(default=0, verbose_name=b'Avg $'),
        ),
    ]
