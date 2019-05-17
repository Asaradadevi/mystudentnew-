# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('studentnew1', '0010_remove_mark_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='First_name',
            field=models.CharField(default=datetime.datetime(2019, 5, 10, 14, 21, 44, 470560, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
    ]
