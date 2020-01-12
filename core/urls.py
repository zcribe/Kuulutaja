from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search/', SearchResultsView.as_view(), name='search-results'),
    path('category/<str:slug>/', CategoryView.as_view(), name='category'),
    path('advertisement/create/', AdvertCreateView.as_view(), name='ad-create'),
    path('advertisement/<str:slug>/', AdvertDetailView.as_view(), name='ad-detail'),
    path('advertisement/<str:slug>/update/', AdvertUpdateView.as_view(), name='ad-update'),
    path('advertisement/<str:slug>/delete/', AdvertDeleteView.as_view(), name='ad-delete'),
    # path('advertisement/all/', AdvertListView.as_view(), name='ad-list'),

]
