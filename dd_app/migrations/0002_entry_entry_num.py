# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dd_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='entry_num',
            field=models.IntegerField(default=0),
        ),
    ]