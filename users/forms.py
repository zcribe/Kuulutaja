from django.contrib.auth import get_user_model
from django import forms


class SignupForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name']

    def save(self, user):
        user.save()
