# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20141024_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosuser',
            name='photo',
            field=models.ImageField(upload_to='perfiles/', null=True, blank=True),
            preserve_default=True,
        ),
    ]
