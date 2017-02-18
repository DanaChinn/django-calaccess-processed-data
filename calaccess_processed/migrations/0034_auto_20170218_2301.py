# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 23:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calaccess_processed', '0033_auto_20170213_0542'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='processeddatafile',
            options={'ordering': ('-version_id', 'file_name'), 'verbose_name': 'TRACKING: processed CAL-ACCESS data file'},
        ),
        migrations.AlterModelOptions(
            name='processeddataversion',
            options={'get_latest_by': 'process_start_datetime', 'ordering': ('-process_start_datetime',), 'verbose_name': 'TRACKING: CAL-ACCESS processed data version'},
        ),
    ]
