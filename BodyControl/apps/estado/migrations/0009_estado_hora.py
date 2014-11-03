# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0008_remove_estado_total_calorias'),
    ]

    operations = [
        migrations.AddField(
            model_name='estado',
            name='hora',
            field=models.DateTimeField(default=datetime.date(2014, 10, 13), auto_now=True),
            preserve_default=False,
        ),
    ]
