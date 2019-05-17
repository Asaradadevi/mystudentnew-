# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentnew1', '0009_remove_mark_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mark',
            name='subject',
        ),
    ]
