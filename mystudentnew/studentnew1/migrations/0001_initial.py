# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ut1_mark', models.PositiveIntegerField()),
                ('ut2_mark', models.PositiveIntegerField()),
                ('ut3_mark', models.PositiveIntegerField()),
                ('Status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('First_name', models.CharField(max_length=20)),
                ('Last_name', models.CharField(max_length=20)),
                ('Register_number', models.PositiveIntegerField()),
                ('Enrolled_year', models.PositiveIntegerField()),
                ('Course', models.CharField(max_length=2)),
                ('Branch', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Subject_code', models.PositiveIntegerField()),
                ('Subject_title', models.CharField(max_length=20)),
                ('Faculty_name', models.CharField(max_length=20)),
                ('Semester', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='marks',
            name='student',
            field=models.ForeignKey(to='studentnew1.Student'),
        ),
        migrations.AddField(
            model_name='marks',
            name='subject',
            field=models.ForeignKey(to='studentnew1.Subject'),
        ),
    ]
