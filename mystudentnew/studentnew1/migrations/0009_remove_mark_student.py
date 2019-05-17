# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentnew1', '0008_auto_20190510_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mark',
            name='student',
        ),
    ]
