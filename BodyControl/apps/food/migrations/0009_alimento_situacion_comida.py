# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0008_auto_20141025_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='alimento',
            name='situacion_comida',
            field=models.CharField(default='', max_length=50),
            preserve_default=True,
        ),
    ]
