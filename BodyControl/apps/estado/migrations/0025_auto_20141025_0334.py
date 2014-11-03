# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0024_auto_20141024_1759'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estado',
            old_name='miDia',
            new_name='midia',
        ),
    ]
