# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='sub_category_name',
            field=models.CharField(max_length=30, verbose_name='название'),
        ),
    ]
