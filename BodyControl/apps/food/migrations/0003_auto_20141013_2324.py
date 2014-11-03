# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20141013_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimento',
            name='tipo',
            field=models.CharField(max_length=50, default=''),
        ),
    ]
