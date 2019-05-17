# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('studentnew1', '0003_auto_20190502_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat1_mark',
            name='Subject_title',
            field=models.CharField(default=datetime.datetime(2019, 5, 2, 22, 58, 19, 640902, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cat2_mark',
            name='Subject_title',
            field=models.CharField(default=datetime.datetime(2019, 5, 2, 22, 58, 48, 169707, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cat3_mark',
            name='Subject_title',
            field=models.CharField(default=datetime.datetime(2019, 5, 2, 22, 59, 6, 964107, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cat1_mark',
            name='cat1_mark',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='cat2_mark',
            name='cat2_mark',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='cat3_mark',
            name='cat3_mark',
            field=models.CharField(max_length=3),
        ),
    ]
