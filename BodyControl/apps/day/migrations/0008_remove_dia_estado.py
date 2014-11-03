# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('day', '0007_auto_20141013_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dia',
            name='estado',
        ),
    ]
