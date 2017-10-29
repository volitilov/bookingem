from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.utils.translation import ugettext as _

from .models import Book, Category, SubCategory

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class Home(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.order_by('id')
        return context



class BooksListView(ListView):
    paginate_by = 1
    books = None
    category = None
    sub_category = None
    sub_categories = None

    def get(self, request, **kwargs):
        self.category = Category.objects.get(category_name=self.kwargs['cat_name'])
        self.sub_categories = self.category.subcategory_set.order_by('id')
        if self.kwargs['sub_cat_name'] == None:
            self.sub_category = self.sub_categories.first()
            self.books = self.sub_category.book_set.order_by('book_title')
        else:
            self.sub_category = SubCategory.objects.get(sub_category_name=self.kwargs['sub_cat_name'])
            self.books = self.sub_category.book_set.order_by('book_title')
        return super().get(request, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.sub_category.sub_category_name
        context['categories'] = Category.objects.order_by('id')
        context['sub_category'] = self.sub_category.sub_category_name
        context['sub_categories'] = self.sub_categories
        context['books'] = self.books
        context['category'] = self.category.category_name
        return context

    def get_queryset(self):
        return self.books