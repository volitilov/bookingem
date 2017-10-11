from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, View

from .models import Tag, Book

# ::::::::::::::::::::::::::::::::::::::::::::::::::::

def index(request):
    data = {
        'title': 'Home',
        'tags': Tag.objects.all()
    }
    if request.POST:
        return render(request, 'results.html')

    return render(request, 'index.html', data)


def results(request):
    data = {
        'title': 'Results',
        'tag': get_object_or_404(Tag, name=name)
    }  
    return render(request, 'results.html', data)


class BookListView(ListView):
    model = Book


class TestView(TemplateView):
    template_name = 'test.html'


class ExView(View):
    def get(self, request):
        return HttpResponse('This get request')
    def post(self, request):
        return HttpResponse('This post request')