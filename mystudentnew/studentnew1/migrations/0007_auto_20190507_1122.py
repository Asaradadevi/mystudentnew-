# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentnew1', '0006_auto_20190503_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mark',
            name='cat1_status',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='cat2_status',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='cat3_status',
        ),
    ]
