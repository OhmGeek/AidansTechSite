# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-25 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TechItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TechTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='techitem',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='tech.TechTag'),
        ),
    ]
