# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20141025_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosuser',
            name='photo',
            field=models.ImageField(upload_to='perfiles/', null=True, blank=True),
        ),
    ]
