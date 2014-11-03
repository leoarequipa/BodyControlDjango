# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0011_auto_20141013_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(default=0, max_length=50)),
                ('calorias', models.FloatField(default=0.0, max_length=20)),
                ('tipo', models.CharField(default=0, max_length=50)),
                ('estado', models.ForeignKey(to='estado.Estado')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
