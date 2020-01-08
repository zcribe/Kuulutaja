from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from users.models import Profile

User = get_user_model()


@receiver(post_save, sender=User, weak=False, dispatch_uid='models.create_profile')
def create_profile(sender, instance, created, **kwargs):
    """ Creates profile object for the user after the user is created """
    if created:
        Profile.objects.create(user=instance)
        print("Created")
