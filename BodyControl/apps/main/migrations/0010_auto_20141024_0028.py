# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20141023_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosuser',
            name='photo',
            field=models.FileField(upload_to='perfiles'),
        ),
    ]
