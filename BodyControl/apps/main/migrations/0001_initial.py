# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosUser',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('edad', models.IntegerField(default=True, max_length=40)),
                ('estatura', models.IntegerField(default=True, max_length=30)),
                ('peso_inicial', models.FloatField(default=0.0, max_length=20)),
                ('peso_ideal', models.FloatField(default=0.0, max_length=20)),
                ('peso_actual', models.FloatField(default=0.0, max_length=20)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
