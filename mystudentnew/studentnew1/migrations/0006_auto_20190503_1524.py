# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentnew1', '0005_auto_20190503_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Register_number', models.PositiveIntegerField()),
                ('Subject_title', models.CharField(max_length=50)),
                ('cat1_mark', models.CharField(max_length=3)),
                ('cat1_status', models.CharField(max_length=30)),
                ('cat2_mark', models.CharField(max_length=3)),
                ('cat2_status', models.CharField(max_length=30)),
                ('cat3_mark', models.CharField(max_length=3)),
                ('cat3_status', models.CharField(max_length=30)),
                ('student', models.ForeignKey(to='studentnew1.Student')),
                ('subject', models.ForeignKey(to='studentnew1.Subject')),
            ],
        ),
        migrations.RemoveField(
            model_name='cat1_mark',
            name='student',
        ),
        migrations.RemoveField(
            model_name='cat1_mark',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='cat2_mark',
            name='student',
        ),
        migrations.RemoveField(
            model_name='cat2_mark',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='cat3_mark',
            name='student',
        ),
        migrations.RemoveField(
            model_name='cat3_mark',
            name='subject',
        ),
        migrations.DeleteModel(
            name='Cat1_Mark',
        ),
        migrations.DeleteModel(
            name='Cat2_Mark',
        ),
        migrations.DeleteModel(
            name='Cat3_Mark',
        ),
    ]
