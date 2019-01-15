# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-01-08 04:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0002_auto_20190104_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='address',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='entry_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='roles',
            field=models.ManyToManyField(null=True, to='rbac.Role'),
        ),
    ]
