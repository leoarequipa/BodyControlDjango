# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_auto_20141013_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='alimento',
            name='puntaje',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
