# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0006_auto_20141013_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estado',
            name='hora',
        ),
    ]
