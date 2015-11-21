# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(default=0)),
                ('highest_bsf', models.IntegerField(default=0)),
                ('avg_earnings', models.FloatField(default=0)),
                ('avg_speed', models.IntegerField(default=0)),
                ('lifetime_win_perc', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Horse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name=b'date')),
                ('race_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='horse',
            field=models.ForeignKey(to='dd_app.Horse'),
        ),
        migrations.AddField(
            model_name='entry',
            name='race',
            field=models.ForeignKey(to='dd_app.Race'),
        ),
    ]
