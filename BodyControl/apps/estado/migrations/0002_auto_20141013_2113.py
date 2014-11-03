# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estado',
            name='estatura',
            field=models.FloatField(max_length=30, default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estado',
            name='peso_actua',
            field=models.FloatField(max_length=30, default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estado',
            name='peso_ideal',
            field=models.FloatField(max_length=30, default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estado',
            name='peso_inicial',
            field=models.FloatField(max_length=20, default=0.0),
            preserve_default=False,
        ),
    ]
