from django.db import models
from django.contrib.auth import get_user_model

from model_utils.models import TimeStampedModel


class Profile(TimeStampedModel):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

