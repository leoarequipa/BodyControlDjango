# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('day', '0003_remove_dia_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='dia',
            name='fecha',
            field=models.DateField(blank=True, default=datetime.datetime.now),
            preserve_default=True,
        ),
    ]
