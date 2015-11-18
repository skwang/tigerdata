# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tigredata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='degree',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='student',
            name='homecity',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='student',
            name='homecountry',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='student',
            name='room',
            field=models.CharField(max_length=64),
        ),
    ]
