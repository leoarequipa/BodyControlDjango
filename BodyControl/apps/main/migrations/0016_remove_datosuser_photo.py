# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20141024_0110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosuser',
            name='photo',
        ),
    ]
