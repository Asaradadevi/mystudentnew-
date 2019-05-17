# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentnew1', '0007_auto_20190507_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='Register_number',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mark',
            name='cat1_mark',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mark',
            name='cat2_mark',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mark',
            name='cat3_mark',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='subject',
            name='Semester',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
