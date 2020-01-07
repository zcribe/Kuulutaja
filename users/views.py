from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from core.models import Advertisement
from .models import Profile


@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.filter(user__username=self.request.user.get_username())
        context['my_adverts'] = Advertisement.objects.filter(owner=self.request.user.pk)
        return context


@method_decorator(login_required, name='dispatch')
class ProfileEmailView(TemplateView):
    template_name = 'users/profile_email.html'


@method_decorator(login_required, name='dispatch')
class ProfilePasswordView(TemplateView):
    template_name = 'users/profile_password.html'


@method_decorator(login_required, name='dispatch')
class ProfileSettingsView(TemplateView):
    template_name = 'users/profile_settings.html'


@method_decorator(login_required, name='dispatch')
class ProfilePrivacyView(TemplateView):
    template_name = 'users/profile_privacy.html'
