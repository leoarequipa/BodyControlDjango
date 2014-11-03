# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('day', '0008_remove_dia_estado'),
        ('estado', '0016_auto_20141016_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='estado',
            name='dia',
            field=models.ForeignKey(to='day.Dia', default=datetime.date(2014, 10, 16)),
            preserve_default=False,
        ),
    ]
