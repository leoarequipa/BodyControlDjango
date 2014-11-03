# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0019_auto_20141016_2322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estado',
            old_name='dia',
            new_name='fecha',
        ),
    ]
