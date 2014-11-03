# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20141024_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosuser',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='perfiles/'),
        ),
    ]
