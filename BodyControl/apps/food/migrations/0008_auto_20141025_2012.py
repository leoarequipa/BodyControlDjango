# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_alimento_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimento',
            name='comentario',
            field=models.TextField(max_length=800, default=''),
        ),
    ]
