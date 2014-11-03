# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20141024_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosuser',
            name='photo',
            field=models.ImageField(upload_to='perfiles/', blank=True, null=True),
        ),
    ]
