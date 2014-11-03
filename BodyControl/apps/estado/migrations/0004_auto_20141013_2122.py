# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0003_auto_20141013_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='estado',
            name='estatura',
            field=models.FloatField(default=0.0, max_length=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estado',
            name='peso_actua',
            field=models.FloatField(default=0.0, max_length=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estado',
            name='peso_ideal',
            field=models.FloatField(default=0.0, max_length=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estado',
            name='peso_inicial',
            field=models.FloatField(default=0.0, max_length=20),
            preserve_default=True,
        ),
    ]
