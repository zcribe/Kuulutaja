from django.contrib.auth import get_user_model

import pytest

from users.models import Profile


@pytest.mark.django_db
def test_profile_create():
    Profile.objects.create()
    assert Profile.objects.count() >= 1


@pytest.mark.django_db
def test_profile_is_created_with_user_create():
    get_user_model().objects.create()
    user = get_user_model().objects.first().pk
    profile = Profile.objects.filter(user=user)
    assert profile is not None
