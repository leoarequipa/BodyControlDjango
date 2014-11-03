# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0022_estado_midia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estado',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='estado',
            name='hora',
        ),
    ]
