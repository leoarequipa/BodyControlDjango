# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_remove_datosuser_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosuser',
            name='eliminado',
            field=models.CharField(default='', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datosuser',
            name='edad',
            field=models.IntegerField(default=0.0, max_length=40),
        ),
        migrations.AlterField(
            model_name='datosuser',
            name='estatura',
            field=models.IntegerField(default=0.0, max_length=30),
        ),
    ]
