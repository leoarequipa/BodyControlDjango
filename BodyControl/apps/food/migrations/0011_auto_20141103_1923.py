# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0010_auto_20141103_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='alimento',
            name='calorias',
            field=models.FloatField(max_length=20, default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alimento',
            name='comentario',
            field=models.TextField(max_length=800, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alimento',
            name='eliminado',
            field=models.CharField(max_length=50, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alimento',
            name='nombre',
            field=models.CharField(max_length=50, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alimento',
            name='photo_food',
            field=models.ImageField(blank=True, upload_to='foods/', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alimento',
            name='puntaje',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alimento',
            name='situacion_comida',
            field=models.CharField(max_length=50, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alimento',
            name='tipo',
            field=models.CharField(max_length=50, default=''),
            preserve_default=True,
        ),
    ]
