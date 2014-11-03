# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('day', '0005_remove_dia_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dia',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='dia',
            name='peso_acumulado',
        ),
        migrations.RemoveField(
            model_name='dia',
            name='peso_dia_ant',
        ),
    ]
