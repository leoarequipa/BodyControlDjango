# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_alimento_eliminado'),
    ]

    operations = [
        migrations.AddField(
            model_name='alimento',
            name='photo_food',
            field=models.ImageField(null=True, upload_to='foods/', blank=True),
            preserve_default=True,
        ),
    ]
