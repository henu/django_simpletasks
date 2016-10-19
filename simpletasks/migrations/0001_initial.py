# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('func', models.TextField()),
                ('args', models.TextField()),
                ('start_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('expires_at', models.DateTimeField(default=None, null=True, blank=True)),
                ('timeout', models.DurationField(default=None, null=True, blank=True)),
                ('started_at', models.DateTimeField(default=None, null=True, blank=True)),
                ('finished_at', models.DateTimeField(default=None, null=True, blank=True)),
                ('error', models.BooleanField(default=False)),
                ('output', models.TextField()),
                ('scheduled_task', models.ForeignKey(related_name='tasks', to='simpletasks.ScheduledTask')),
            ],
        ),
    ]
