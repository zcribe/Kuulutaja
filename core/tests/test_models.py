from datetime import datetime, timezone

import pytest
from django.contrib.auth import get_user_model

from ..models import Category, Advertisement, AdvertisementImage
from ..factories import  category_factory, AdvertisementFactoryStatic, AdvertisementImageFactoryStatic


@pytest.mark.django_db
def test_category_create():
    category_factory(2)
    assert Category.objects.count() >= 1


@pytest.mark.django_db
def test_advertisement_create():
    AdvertisementFactoryStatic.create()
    assert Advertisement.objects.count() == 1


@pytest.mark.django_db
def test_advertisement_image_create():
    AdvertisementImageFactoryStatic.create()
    assert AdvertisementImage.objects.count() == 1
