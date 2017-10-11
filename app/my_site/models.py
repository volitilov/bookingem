from django.db import models
from django.utils import timezone
from django.conf import settings

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Category(models.Model):
	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'

	name = models.CharField( max_length=30, verbose_name='Название', unique=True)

	def __str__(self):
		return self.name



class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=30, verbose_name='Tag', unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
	class Meta():
		verbose_name = 'Book'
		verbose_name_plural = 'Books'

	title = models.CharField(max_length=200, verbose_name='Название:')
	description = models.TextField(verbose_name='Описание:')
	category = models.ManyToManyField(Category, verbose_name='Категория(и):')
	tags = models.ManyToManyField(Tag, verbose_name='Tags:')
	img_small = models.ImageField(upload_to='books/%d-%m-%Y', verbose_name='Мал. изображение:')
	img_big = models.ImageField(upload_to='books/%d-%m-%Y', verbose_name='Бол. изображение:')
	download_link = models.URLField(max_length=300, verbose_name='Ссылка скачки:')
	created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания:')
	published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации:')
	likes = models.IntegerField(default=0, verbose_name='Кол. лайков:')
	previews = models.IntegerField(default=0, verbose_name='Кол. просмотров:')

	def __str__(self):
		return self.title
