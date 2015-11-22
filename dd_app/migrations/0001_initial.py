# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BSF',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entry_num', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('highest_bsf', models.IntegerField(default=0)),
                ('avg_earnings', models.FloatField(default=0)),
                ('avg_speed', models.FloatField(default=-1)),
                ('lifetime_win_perc', models.FloatField(default=0)),
            ],
            options={
                'ordering': ['entry_num'],
            },
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
                ('race_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Raceday',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='race',
            name='day',
            field=models.ForeignKey(to='dd_app.Raceday'),
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
        migrations.AddField(
            model_name='bsf',
            name='entry',
            field=models.ForeignKey(to='dd_app.Entry'),
        ),
    ]
