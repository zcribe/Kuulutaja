from django.contrib.auth import get_user_model
from django import forms
from allauth.account.forms import SignupForm


class ModifiedSignupForm(SignupForm):
    def signup(self, request):
        user = super(ModifiedSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        user.profile.bio = self.cleaned_data['bio']
        user.profile.save()
        return user
