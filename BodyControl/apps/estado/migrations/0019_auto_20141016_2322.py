# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0018_auto_20141016_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estado',
            name='fecha',
        ),
        migrations.AlterField(
            model_name='estado',
            name='dia',
            field=models.DateTimeField(),
        ),
    ]
