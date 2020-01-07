from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Profile


@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.filter(user__username=self.request.user.get_username())
        return context
