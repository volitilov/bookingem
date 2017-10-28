from django.http import HttpRequest
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.contrib import messages

from .models import Book, Category, SubCategory
from .forms import BookForm

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class BookEdit(TemplateView):
    form = None
    sub_category = None
    book = None

    def get(self, request, **kwargs):
        self.book = Book.objects.get(title=self.kwargs['title'])
        self.sub_category = self.book.book_sub_category
        self.form = BookForm(instance=self.post)
        return super().get(request, **kwargs)

    def post(self, request, **kwargs):
        book = Book.objects.get(title=self.kwargs['title'])
        self.form = BookForm(request.POST, request.FILES, instance=post)
        if self.form.is_valid():
            self.form.save()
            messages.success(request, 'Книга успешно изменена.')
            return redirect(self.request.session['prev_page'])
        else:
            return super().post(request, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        context['prev_page'] = self.request.session['prev_page']
        context['categories'] = SubCategory.objects.order_by('id')
        return context



class BookDelete(TemplateView):
    def post(self, request, **kwargs):
        Book.objects.get(title=self.kwargs['title']).delete()
        messages.success(request, 'Книга успешно удалёна.')
        return redirect(self.request.session['prev_page'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prev_page'] = self.request.session['prev_page']
        context['categories'] = Category.objects.order_by('id')
        return context
