from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from django.db.models import Prefetch
from django.contrib.postgres.search import TrigramSimilarity


from allauth.account.decorators import verified_email_required

from .models import Category, Advertisement, AdvertisementImage


class IndexView(ListView):
    model = Category
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['annotated_list'] = Category.get_annotated_list()
        context['latest'] = Advertisement.public.prefetch_related('advertisement')[:10]
        return context


class AdvertListView(ListView):
    model = Advertisement
    template_name = 'core/advert_list.html'

    def get_context_data(self, **kwargs):
        context = super(AdvertListView, self).get_context_data(**kwargs)
        # context['annotated_list'] = Advertisement.objects.annotate(similarity=TrigramSimilarity('name', self.))
        return context


class AdvertDetailView(DetailView):
    """ Read Ad"""
    model = Advertisement
    template_name = 'core/advert_detail.html'


class CategoryView(ListView):
    model = Advertisement
    template_name = 'core/category_list.html'

    def get_queryset(self):
        return Advertisement.public.filter(category__slug__iexact=self.kwargs['slug'])


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
            location_vector = SearchVector('location_city', weight='C')
            core_vector = name_vector + content_vector + location_vector
            queryset = queryset.annotate(search=core_vector).filter(search=query)
            queryset = queryset.annotate(rank=SearchRank(core_vector, query)).order_by('-rank')
        return queryset


@method_decorator(login_required, name='dispatch')
class AdvertCreateView(CreateView):
    """ Create Ad"""
    model = Advertisement
    template_name = 'core/advert_create.html'
    fields = ['name', 'contact_email', 'contact_phone', 'category', 'content', 'price', 'location_city', 'expires_date']
    success_url = '/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


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
