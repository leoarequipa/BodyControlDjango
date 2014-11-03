# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0010_auto_20141013_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='hora',
            field=models.DateTimeField(),
        ),
    ]
