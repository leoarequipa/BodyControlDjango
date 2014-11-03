# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('estado', '0012_remove_estado_persona'),
    ]

    operations = [
        migrations.AddField(
            model_name='estado',
            name='persona',
            field=models.DateField(blank=True, default=datetime.datetime.now),
            preserve_default=False,
        ),
    ]
