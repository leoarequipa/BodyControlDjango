# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20141025_0237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datosuser',
            old_name='photo',
            new_name='avatar',
        ),
        migrations.AddField(
            model_name='datosuser',
            name='sexo',
            field=models.CharField(default='', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datosuser',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
