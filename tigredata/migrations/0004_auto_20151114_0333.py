# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tigredata', '0003_auto_20151114_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='firstname',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='student',
            name='hall',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='student',
            name='lastname',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='student',
            name='netid',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='student',
            name='rescollege',
            field=models.CharField(max_length=64),
        ),
    ]
