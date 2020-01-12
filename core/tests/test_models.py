import pytest
from django.contrib.auth import get_user_model

from ..models import Category, Advertisement, AdvertisementImage
from ..factories import AdvertisementFactory, AdvertisementImageFactory, category_factory


@pytest.mark.django_db
def test_category_create():
    category_factory(2)
    assert Category.objects.count() >= 1


@pytest.mark.django_db
def test_advertisement_create():
    AdvertisementFactory.create()
    assert Advertisement.objects.count() == 1


@pytest.mark.django_db
def test_advertisement_image_create():
    AdvertisementImageFactory.create()
    assert AdvertisementImage.objects.count() == 1
