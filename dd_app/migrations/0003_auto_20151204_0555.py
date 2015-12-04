# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dd_app', '0002_auto_20151122_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='score_perc',
            field=models.FloatField(default=0, verbose_name=b'Score %'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='avg_earnings',
            field=models.FloatField(default=0, verbose_name=b'Avg Earnings'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='avg_speed',
            field=models.FloatField(default=-1, verbose_name=b'Avg Speed'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='entry_num',
            field=models.IntegerField(default=0, verbose_name=b'Entry'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='highest_bsf',
            field=models.IntegerField(default=0, verbose_name=b'Highest BSF'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='horse',
            field=models.ForeignKey(verbose_name=b'Horse', to='dd_app.Horse'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='lifetime_win_perc',
            field=models.FloatField(default=0, verbose_name=b'Lifetime Win %'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='score',
            field=models.IntegerField(default=0, verbose_name=b'Score'),
        ),
    ]
