# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentnew1', '0004_auto_20190502_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Enrolled_year',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='Register_number',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
