# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0002_auto_20141013_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estado',
            name='estatura',
        ),
        migrations.RemoveField(
            model_name='estado',
            name='peso_actua',
        ),
        migrations.RemoveField(
            model_name='estado',
            name='peso_ideal',
        ),
        migrations.RemoveField(
            model_name='estado',
            name='peso_inicial',
        ),
    ]
