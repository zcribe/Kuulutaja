from django.db import models
from django.contrib.auth import get_user_model

from phonenumber_field.modelfields import PhoneNumberField
from model_utils.models import TimeStampedModel


class Profile(TimeStampedModel):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    locations = models.CharField(max_length=100, blank=True, null=True)
