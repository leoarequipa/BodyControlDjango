# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('day', '0009_dia_autocritica'),
        ('estado', '0021_estado_comida'),
    ]

    operations = [
        migrations.AddField(
            model_name='estado',
            name='miDia',
            field=models.ForeignKey(null=True, to='day.Dia'),
            preserve_default=True,
        ),
    ]
