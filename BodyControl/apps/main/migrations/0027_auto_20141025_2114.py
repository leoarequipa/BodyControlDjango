# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_datosuser_situacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datosuser',
            old_name='situacion',
            new_name='situacion_general',
        ),
    ]
