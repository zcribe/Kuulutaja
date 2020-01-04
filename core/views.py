from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank

from .models import Category, Advertisement


class IndexView(ListView):
    model = Category
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['annotated_list'] = Category.get_annotated_list()
        context['ads'] = Advertisement.public.get_queryset()[:30]
        return context


class AdvertListView(ListView):
    model = Advertisement
    template_name = 'core/advert_list.html'


class AdvertDetailView(DetailView):
    """ Read Ad"""
    model = Advertisement
    template_name = 'core/advert_detail.html'


class SearchResultsView(ListView):
    """ Display Advertisements filtered by the search """
    model = Advertisement
    paginate_by = 20
    template_name = 'core/search_results.html'

    def get_queryset(self):
        queryset = Advertisement.public.get_queryset()
        search_terms = self.request.GET.get('q')

        if search_terms:
            query = SearchQuery(search_terms)
            name_vector = SearchVector('name', weight='A')
            content_vector = SearchVector('content', weight='B')
            core_vector = name_vector + content_vector
            queryset = queryset.annotate(search=core_vector).filter(search=query)
            queryset = queryset.annotate(rank=SearchRank(core_vector, query)).order_by('-rank')
        return queryset




@method_decorator(login_required, name='dispatch')
class AdvertCreateView(CreateView):
    """ Create Ad"""
    model = Advertisement
    template_name = 'core/advert_create.html'


@method_decorator(login_required, name='dispatch')
class AdvertDeleteView(DeleteView):
    """ Delete Ad """
    model = Advertisement
    template_name = 'core/advert_delete.html'


@method_decorator(login_required, name='dispatch')
class AdvertUpdateView(UpdateView):
    """ Update Ad """
    model = Advertisement
    template_name = 'core/advert_update.html'
