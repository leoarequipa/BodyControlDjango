# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_alimento_puntaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='alimento',
            name='eliminado',
            field=models.CharField(default='', max_length=50),
            preserve_default=True,
        ),
    ]
