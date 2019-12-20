from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Category, SubCategory, Advertisement


class CategoryView(ListView):
    model = Category
    template_name = 'core/category_list.html'


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
