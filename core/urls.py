from django.urls import path
from .views import *

urlpatterns = [
    path('advertisement/', AdvertListView.as_view(), name='ad-list'),
    path('advertisement/<str:slug>/', AdvertDetailView.as_view(), name='ad-detail'),
    path('advertisement/<str:slug>/create/', AdvertCreateView.as_view(), name='ad-create'),
    path('advertisement/<str:slug>/update/', AdvertUpdateView.as_view(), name='ad-update'),
    path('advertisement/<str:slug>/delete/', AdvertDeleteView.as_view(), name='ad-delete'),

]