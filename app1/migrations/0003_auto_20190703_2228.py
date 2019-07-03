# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20190703_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtimenum',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 3, 14, 28, 0, 923000, tzinfo=utc), verbose_name=b'create time', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='savednum',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 3, 14, 28, 6, 139000, tzinfo=utc), verbose_name=b'create time', auto_now_add=True),
            preserve_default=False,
        ),
    ]
