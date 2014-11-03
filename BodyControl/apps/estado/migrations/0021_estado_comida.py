# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0020_auto_20141016_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='estado',
            name='comida',
            field=models.CharField(max_length=50, default=True),
            preserve_default=True,
        ),
    ]
