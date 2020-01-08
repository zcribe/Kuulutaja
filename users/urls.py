from django.urls import path
from .views import *

urlpatterns = [
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('accounts/profile/email', ProfileEmailView.as_view(), name='profile-email'),
    path('accounts/profile/update', ProfileUpdateView.as_view(), name='profile-update'),
    path('accounts/profile/password', ProfilePasswordView.as_view(), name='profile-password'),
    path('accounts/profile/settings', ProfileSettingsView.as_view(), name='profile-settings'),
    path('accounts/profile/privacy', ProfilePrivacyView.as_view(), name='profile-privacy'),
]
