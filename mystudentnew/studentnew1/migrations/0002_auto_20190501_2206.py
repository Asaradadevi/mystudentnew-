# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentnew1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Register_number', models.PositiveIntegerField()),
                ('ut1_mark', models.PositiveIntegerField()),
                ('ut2_mark', models.PositiveIntegerField()),
                ('ut3_mark', models.PositiveIntegerField()),
                ('Status', models.CharField(max_length=20)),
                ('student', models.ForeignKey(to='studentnew1.Student')),
                ('subject', models.ForeignKey(to='studentnew1.Subject')),
            ],
        ),
        migrations.RemoveField(
            model_name='marks',
            name='student',
        ),
        migrations.RemoveField(
            model_name='marks',
            name='subject',
        ),
        migrations.DeleteModel(
            name='Marks',
        ),
    ]
