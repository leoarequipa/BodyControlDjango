# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('day', '0004_dia_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dia',
            name='fecha',
        ),
    ]
