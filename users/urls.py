from django.urls import path
from .views import *

urlpatterns = [
    path('accounts/profile', ProfileView.as_view(), name='profile'),
]
