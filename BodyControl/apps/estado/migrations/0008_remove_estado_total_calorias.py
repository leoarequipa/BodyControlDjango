# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0007_remove_estado_hora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estado',
            name='total_calorias',
        ),
    ]
