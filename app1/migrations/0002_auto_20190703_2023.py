# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtimenum',
            name='val',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='savednum',
            name='val',
            field=models.FloatField(),
        ),
    ]
