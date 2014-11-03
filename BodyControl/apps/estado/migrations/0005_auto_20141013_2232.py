# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0004_auto_20141013_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estado',
            name='estatura',
        ),
 
        migrations.RemoveField(
            model_name='estado',
            name='total_calorias',
        ),
        migrations.RemoveField(
            model_name='estado',
            name='peso_ideal',
        ),
        migrations.RemoveField(
            model_name='estado',
            name='peso_inicial',
        ),
          migrations.AddField(
            model_name='estado',
            name='hora',
            field=models.DateField(blank=True, default=datetime.datetime.now),
            preserve_default=True,
 
        ),
      
        migrations.AddField(
            model_name='estado',
            name='total_calorias',
            field=models.IntegerField(max_length=30),
            preserve_default=True,
        ),
    ]
