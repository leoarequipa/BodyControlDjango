# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0014_remove_estado_persona'),
    ]

    operations = [
        migrations.AddField(
            model_name='estado',
            name='persona',
            field=models.DateTimeField(default=datetime.date(2014, 10, 16)),
            preserve_default=False,
        ),
    ]
