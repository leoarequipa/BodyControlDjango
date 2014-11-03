# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('titulo', models.CharField(max_length=50, default='')),
                ('contenido', models.CharField(max_length=500, default='')),
                ('photo', models.ImageField(null=True, upload_to='recommendation/', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
