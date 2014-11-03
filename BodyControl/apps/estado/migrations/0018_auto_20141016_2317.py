# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0017_estado_dia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='dia',
            field=models.ForeignKey(null=True, to='day.Dia'),
        ),
    ]
