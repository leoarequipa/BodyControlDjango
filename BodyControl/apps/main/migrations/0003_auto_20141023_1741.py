# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_datosuser_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosuser',
            name='photo',
            field=models.FileField(upload_to='pic_folder/'),
        ),
    ]
