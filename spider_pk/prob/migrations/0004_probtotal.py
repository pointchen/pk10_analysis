# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 02:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prob', '0003_auto_20171109_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProbTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('probtotal_rule', models.CharField(max_length=100)),
                ('probtotal_amount', models.FloatField()),
                ('probtotal_win', models.FloatField()),
                ('probtotal_lose', models.FloatField()),
                ('probtotal_gain', models.FloatField()),
            ],
        ),
    ]
