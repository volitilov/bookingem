from django.db import models
from django.utils import timezone

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Category(models.Model):
    class Meta:
        db_table = 'book_categories'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    category_name = models.CharField(max_length=30, unique=True, verbose_name='название')

    def __str__(self):
        return self.category_name




class SubCategory(models.Model):
    class Meta:
        db_table = 'sub_book_categories'
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'

    sub_category_name = models.CharField(max_length=30, verbose_name='название')
    parent_category = models.ForeignKey(Category, verbose_name='категория')

    def __str__(self):
        return self.sub_category_name




class Book(models.Model):
    class Meta:
        db_table = 'book'
        verbose_name = 'книга'
        verbose_name_plural = 'книги'
    
    book_title = models.CharField(max_length=50, db_index=True, 
                    unique=True, verbose_name='название')
    book_author = models.CharField(max_length=50, verbose_name='автор издания')
    book_publish_year = models.PositiveSmallIntegerField(verbose_name='год издания')
    book_language = models.CharField(max_length=50, verbose_name='язык книги')
    book_count_page = models.PositiveSmallIntegerField(verbose_name='кол-во страниц')
    book_type = models.CharField(max_length=50, verbose_name='тип книги')
    book_size = models.PositiveSmallIntegerField(verbose_name='размер архива')
    book_description = models.TextField(verbose_name='описание')
    book_pub_date = models.DateField(db_index=True, auto_now_add=True, verbose_name='дата публикации')
    book_link_download = models.URLField(verbose_name='ссылка для скачки')
    book_count_downloads = models.IntegerField(default=0, verbose_name='кол-во загрузок')
    book_thumbnail = models.ImageField(upload_to = "books/img", null=True, blank=True)
    book_sub_category = models.ManyToManyField(SubCategory, verbose_name='категория(и)')

    def save(self, *args, **kwargs):
        try:
            this_record = Book.objects.get(id = self.id)
            if this_record.book_thumbnail != self.book_thumbnail:
                this_record.book_thumbnail.delete(save = False)
        except: pass
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.book_thumbnail.delete(save = False)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.book_title
    