from django.conf.urls import url

from .views import BooksListView
from .views2 import BookEdit, BookDelete

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

urlpatterns = [
    url(r'^(?P<cat_name>[\w\s]+)/(?:(?P<sub_cat_name>[\w\s\+\.\#]+)/)?$', 
        BooksListView.as_view(template_name='books.html'), 
        name='books'),
    
    url(r'^book/(?P<title>[\w\s\.]+)/edit$', 
        BookEdit.as_view(template_name='book_edit.html'), 
        name='book_edit'),
    url(r'^book/(?P<title>[\w\s\.]+)/del$', 
        BookDelete.as_view(template_name='book_del.html'), 
        name='book_del'),
]