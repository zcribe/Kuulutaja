from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Category, Advertisement


class IndexView(ListView):
    model = Category
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['annotated_list'] = Category.get_annotated_list()
        context['ads'] = Advertisement.objects.filter(status='published').order_by('published_date')[:100]
        return context


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
