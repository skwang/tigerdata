# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HallList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('halls', jsonfield.fields.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('netid', models.CharField(max_length=32)),
                ('firstname', models.CharField(max_length=32)),
                ('lastname', models.CharField(max_length=32)),
                ('homecity', models.CharField(max_length=32)),
                ('homecountry', models.CharField(max_length=32)),
                ('degree', models.CharField(max_length=32)),
                ('major', models.CharField(max_length=3)),
                ('hall', models.CharField(max_length=32)),
                ('room', models.CharField(max_length=32)),
                ('rescollege', models.CharField(max_length=32)),
                ('classyear', models.CharField(max_length=4)),
            ],
        ),
    ]
