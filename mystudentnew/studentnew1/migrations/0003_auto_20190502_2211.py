# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentnew1', '0002_auto_20190501_2206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat1_Mark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Register_number', models.PositiveIntegerField()),
                ('cat1_mark', models.PositiveIntegerField()),
                ('Status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Cat2_Mark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Register_number', models.PositiveIntegerField()),
                ('cat2_mark', models.PositiveIntegerField()),
                ('Status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Cat3_Mark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Register_number', models.PositiveIntegerField()),
                ('cat3_mark', models.PositiveIntegerField()),
                ('Status', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='mark',
            name='student',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='subject',
        ),
        migrations.AlterField(
            model_name='student',
            name='First_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='Last_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='subject',
            name='Faculty_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='subject',
            name='Subject_code',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='subject',
            name='Subject_title',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Mark',
        ),
        migrations.AddField(
            model_name='cat3_mark',
            name='student',
            field=models.ForeignKey(to='studentnew1.Student'),
        ),
        migrations.AddField(
            model_name='cat3_mark',
            name='subject',
            field=models.ForeignKey(to='studentnew1.Subject'),
        ),
        migrations.AddField(
            model_name='cat2_mark',
            name='student',
            field=models.ForeignKey(to='studentnew1.Student'),
        ),
        migrations.AddField(
            model_name='cat2_mark',
            name='subject',
            field=models.ForeignKey(to='studentnew1.Subject'),
        ),
        migrations.AddField(
            model_name='cat1_mark',
            name='student',
            field=models.ForeignKey(to='studentnew1.Student'),
        ),
        migrations.AddField(
            model_name='cat1_mark',
            name='subject',
            field=models.ForeignKey(to='studentnew1.Subject'),
        ),
    ]
