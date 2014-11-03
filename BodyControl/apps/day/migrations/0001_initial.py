# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('fecha', models.DateField(blank=True, default=datetime.datetime.now)),
                ('peso_dia_ant', models.FloatField(max_length=20, default=0.0)),
                ('peso_acumulado', models.FloatField(max_length=30, default=0.0)),
                ('estado', models.CharField(max_length=50, default=True)),
                ('persona', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
