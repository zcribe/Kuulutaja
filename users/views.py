from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from core.models import Advertisement
from .models import Profile


@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        # context['profile'] = Profile.objects.filter(user=self.request.user.pk)
        context['profile'] = Profile.objects.all().count()
        context['my_adverts'] = Advertisement.objects.filter(owner=self.request.user.pk)
        return context


@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    template_name = 'users/profile_update.html'
    model = Profile
    fields = ['bio']
    success_url = '/accounts/profile'

    def get_object(self, queryset=None):
        obj = Profile.objects.filter(user=self.request.user.pk)
        return obj.get()


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
