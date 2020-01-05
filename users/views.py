from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from . models import Profile


class ProfileView(TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.filter(user__username=self.kwargs['pk'])
        return context
