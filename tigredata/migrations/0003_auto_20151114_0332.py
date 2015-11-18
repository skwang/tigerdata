# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tigredata', '0002_auto_20151114_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='degree',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='student',
            name='major',
            field=models.CharField(max_length=64),
        ),
    ]
