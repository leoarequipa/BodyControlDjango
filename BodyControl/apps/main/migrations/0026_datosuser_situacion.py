# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20141025_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosuser',
            name='situacion',
            field=models.CharField(max_length=50, default=''),
            preserve_default=True,
        ),
    ]
