from django.contrib import admin
from .models import Book, Tag, Category

# :::::::::::::::::::::::::::::::::::::::::::::::::::

admin.site.register(Book)
admin.site.register(Tag)
admin.site.register(Category)
