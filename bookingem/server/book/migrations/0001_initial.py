# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 18:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='название')),
                ('book_author', models.CharField(max_length=50, verbose_name='автор издания')),
                ('book_publish_year', models.PositiveSmallIntegerField(verbose_name='год издания')),
                ('book_language', models.CharField(max_length=50, verbose_name='язык книги')),
                ('book_count_page', models.PositiveSmallIntegerField(verbose_name='кол-во страниц')),
                ('book_type', models.CharField(max_length=50, verbose_name='тип книги')),
                ('book_size', models.PositiveSmallIntegerField(verbose_name='размер архива')),
                ('book_description', models.TextField(verbose_name='описание')),
                ('book_pub_date', models.DateField(auto_now_add=True, db_index=True, verbose_name='дата публикации')),
                ('book_link_download', models.URLField(verbose_name='ссылка для скачки')),
                ('book_count_downloads', models.IntegerField(default=0, verbose_name='кол-во загрузок')),
                ('book_thumbnail', models.ImageField(blank=True, null=True, upload_to='books/img')),
            ],
            options={
                'db_table': 'book',
                'verbose_name_plural': 'книги',
                'verbose_name': 'книга',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30, unique=True, verbose_name='название')),
            ],
            options={
                'db_table': 'book_categories',
                'verbose_name_plural': 'категории',
                'verbose_name': 'категория',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category_name', models.CharField(max_length=30, unique=True, verbose_name='название')),
                ('parent_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Category', verbose_name='категория')),
            ],
            options={
                'db_table': 'sub_book_categories',
                'verbose_name_plural': 'подкатегории',
                'verbose_name': 'подкатегория',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='book_sub_category',
            field=models.ManyToManyField(to='book.SubCategory', verbose_name='категория(и)'),
        ),
    ]