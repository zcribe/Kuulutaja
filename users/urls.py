from django.urls import path
from .views import *

urlpatterns = [
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile')

]
