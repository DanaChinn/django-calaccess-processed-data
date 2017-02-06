# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 16:27
from __future__ import unicode_literals

import calaccess_processed.models.opencivicdata.base
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calaccess_processed', '0024_auto_20170206_0042'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContestBase',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Time that this object was created at in the system.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Time that this object was last updated in the system.')),
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Common to all Open Civic Data types, the value is a key-value store suitable for storing arbitrary information not covered elsewhere.')),
                ('id', calaccess_processed.models.opencivicdata.base.OCDIDField(help_text='Open Civic Data-style id in the format ``ocd-contest/{{uuid}}``.', ocd_type='contest', serialize=False, validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-contest/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-contest/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')])),
                ('name', models.CharField(help_text='Name of the contest, not necessarily as it appears on the ballot.', max_length=300)),
                ('division', models.ForeignKey(help_text='Reference to the OCD ``Division`` that defines the geographical scope of the contest, e.g., a specific Congressional or State Senate district.', on_delete=django.db.models.deletion.CASCADE, related_name='contestbase_contests', to='calaccess_processed.Division')),
                ('election', models.ForeignKey(help_text='Reference to the OCD ``Election`` in which the contest is decided.', on_delete=django.db.models.deletion.CASCADE, related_name='contestbase_contests', to='calaccess_processed.Election')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='BallotMeasureContestIdentifier',
            new_name='ContestIdentifier',
        ),
        migrations.RemoveField(
            model_name='ballotmeasurecontest',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='ballotmeasurecontest',
            name='division',
        ),
        migrations.RemoveField(
            model_name='ballotmeasurecontest',
            name='election',
        ),
        migrations.RemoveField(
            model_name='ballotmeasurecontest',
            name='extras',
        ),
        migrations.RemoveField(
            model_name='ballotmeasurecontest',
            name='id',
        ),
        migrations.RemoveField(
            model_name='ballotmeasurecontest',
            name='name',
        ),
        migrations.RemoveField(
            model_name='ballotmeasurecontest',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='candidatecontest',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='candidatecontest',
            name='division',
        ),
        migrations.RemoveField(
            model_name='candidatecontest',
            name='election',
        ),
        migrations.RemoveField(
            model_name='candidatecontest',
            name='extras',
        ),
        migrations.RemoveField(
            model_name='candidatecontest',
            name='id',
        ),
        migrations.RemoveField(
            model_name='candidatecontest',
            name='name',
        ),
        migrations.RemoveField(
            model_name='candidatecontest',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='contestidentifier',
            name='contest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='identifiers', to='calaccess_processed.ContestBase'),
        ),
        migrations.AddField(
            model_name='ballotmeasurecontest',
            name='contestbase_ptr',
            field=models.OneToOneField(auto_created=True, default='', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='calaccess_processed.ContestBase'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidatecontest',
            name='contestbase_ptr',
            field=models.OneToOneField(auto_created=True, default='', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='calaccess_processed.ContestBase'),
            preserve_default=False,
        ),
    ]
