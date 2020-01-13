from django.urls import path

from django_filters.views import FilterView

from .views import *
from .models import Advertisement

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search/', SearchResultsView.as_view(), name='search-results'),
    path('category/<str:slug>/', CategoryView.as_view(), name='category'),
    path('advertisement/create/', AdvertCreateView.as_view(), name='ad-create'),
    path('advertisement/<str:slug>/', AdvertDetailView.as_view(), name='ad-detail'),
    path('advertisement/<str:slug>/update/', AdvertUpdateView.as_view(), name='ad-update'),
    path('advertisement/<str:slug>/delete/', AdvertDeleteView.as_view(), name='ad-delete'),
    path('advertisement/filter/', FilterView.as_view(model=Advertisement))
    # path('advertisement/all/', AdvertListView.as_view(), name='ad-list'),

]
