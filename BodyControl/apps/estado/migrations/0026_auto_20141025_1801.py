# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0025_auto_20141025_0334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estado',
            old_name='midia',
            new_name='day',
        ),
    ]
