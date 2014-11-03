# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0009_alimento_situacion_comida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alimento',
            name='calorias',
        ),
        migrations.RemoveField(
            model_name='alimento',
            name='comentario',
        ),
        migrations.RemoveField(
            model_name='alimento',
            name='eliminado',
        ),
        migrations.RemoveField(
            model_name='alimento',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='alimento',
            name='photo_food',
        ),
        migrations.RemoveField(
            model_name='alimento',
            name='puntaje',
        ),
        migrations.RemoveField(
            model_name='alimento',
            name='situacion_comida',
        ),
        migrations.RemoveField(
            model_name='alimento',
            name='tipo',
        ),
    ]
