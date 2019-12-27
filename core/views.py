from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Category, Advertisement


class IndexView(ListView):
    model = Category
    template_name = 'core/index.html'


class CategoryView(ListView):
    model = Category
    template_name = 'core/category_list.html'
    category = ''

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        return Category.objects.filter(id=self.kwargs['pk']).prefetch_related('subcategory_set')


class AdvertListView(ListView):
    model = Advertisement
    template_name = 'core/advert_list.html'


class AdvertDetailView(DetailView):
    """ Read Ad"""
    model = Advertisement
    template_name = 'advert_detail.html'


@method_decorator(login_required, name='dispatch')
class AdvertCreateView(CreateView):
    """ Create Ad"""
    model = Advertisement
    template_name = 'advert_create.html'


@method_decorator(login_required, name='dispatch')
class AdvertDeleteView(DeleteView):
    """ Delete Ad """
    model = Advertisement
    template_name = 'advert_delete.html'


@method_decorator(login_required, name='dispatch')
class AdvertUpdateView(UpdateView):
    """ Update Ad """
    model = Advertisement
    template_name = 'advert_update.html'
