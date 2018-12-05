# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-03 09:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('variants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('nucleotide_change', models.CharField(default='', max_length=200)),
                ('protein_change', models.CharField(max_length=100)),
                ('other_mappings', models.TextField(blank=True)),
                ('alias', models.CharField(max_length=80)),
                ('transcripts', models.TextField(blank=True)),
                ('region', models.CharField(max_length=100)),
                ('reported_classification', models.CharField(max_length=100)),
                ('inferred_classification', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=10)),
                ('last_evaluated', models.CharField(max_length=20)),
                ('last_updated', models.CharField(max_length=20)),
                ('url', models.URLField()),
                ('submitter_content', models.TextField(blank=True)),
                ('assembly', models.CharField(max_length=10)),
                ('_chr', models.CharField(max_length=5)),
                ('genomic_start', models.CharField(max_length=20)),
                ('genomic_stop', models.CharField(max_length=20)),
                ('ref', models.CharField(max_length=100)),
                ('alt', models.CharField(max_length=100)),
                ('accession', models.CharField(max_length=20)),
                ('reported_ref', models.CharField(max_length=100)),
                ('reported_alt', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='gene',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='variant',
            name='gene',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variants.Gene'),
        ),
    ]
