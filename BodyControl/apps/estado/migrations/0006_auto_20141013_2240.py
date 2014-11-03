# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0005_auto_20141013_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='hora',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='estado',
            name='total_calorias',
            field=models.IntegerField(max_length=40),
        ),
    ]
