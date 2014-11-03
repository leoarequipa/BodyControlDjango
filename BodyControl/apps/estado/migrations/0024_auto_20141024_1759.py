# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0023_auto_20141017_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='estado',
            name='eliminado',
            field=models.CharField(default='', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estado',
            name='comida',
            field=models.CharField(default='', max_length=50),
        ),
    ]
