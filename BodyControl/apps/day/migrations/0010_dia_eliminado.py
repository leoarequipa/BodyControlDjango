# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('day', '0009_dia_autocritica'),
    ]

    operations = [
        migrations.AddField(
            model_name='dia',
            name='eliminado',
            field=models.CharField(default='', max_length=50),
            preserve_default=True,
        ),
    ]
