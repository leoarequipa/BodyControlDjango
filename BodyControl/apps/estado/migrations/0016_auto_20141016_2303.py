# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0015_estado_persona'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estado',
            old_name='persona',
            new_name='fecha',
        ),
    ]
