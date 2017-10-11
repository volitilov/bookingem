from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from .views import TestView, BookListView, ExView

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::

app_name = 'bkgem'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^results/(?P<name>[^/]+)$', views.results, name='results'),
    url(r'^books/$', BookListView.as_view(), name='books'),
    # url(r'^detail/(?P<name>[a-zA-Z]+)$', views.DetailView, name='detail'),

    url(r'^test$', TestView.as_view(), name='test'),
    url(r'^test2$', TemplateView.as_view(template_name='test.html'), name='test2'),
    url(r'^ex$', ExView.as_view(), name='ex'),
]