# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('day', '0006_auto_20141013_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='dia',
            name='estado',
            field=models.CharField(default=0, max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dia',
            name='fecha',
            field=models.DateTimeField(default=datetime.date(2014, 10, 13)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dia',
            name='peso_acumulado',
            field=models.FloatField(default=0.0, max_length=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dia',
            name='peso_dia_ant',
            field=models.FloatField(default=0.0, max_length=20),
            preserve_default=True,
        ),
    ]
