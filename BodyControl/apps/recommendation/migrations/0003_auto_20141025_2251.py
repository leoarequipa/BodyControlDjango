# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0002_auto_20141025_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='contenido',
            field=models.TextField(max_length=300000, default=''),
        ),
    ]
