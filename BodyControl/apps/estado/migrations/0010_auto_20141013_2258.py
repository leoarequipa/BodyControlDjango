# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0009_estado_hora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estado',
            name='peso_actua',
        ),
        migrations.AddField(
            model_name='estado',
            name='total_calorias',
            field=models.IntegerField(default=True, max_length=40),
            preserve_default=True,
        ),
    ]
