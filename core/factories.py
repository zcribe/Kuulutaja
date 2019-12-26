import random

import factory
from django.contrib.auth.models import User

from .models import Category, SubCategory, Advertisement, AdvertisementImage

LOCALE = 'et'
TIMEZONE = 'Europe/Tallinn'


class CategoryFactory(factory.django.DjangoModelFactory):
    """ Generates dummy category object """
    name = factory.Faker('word')

    class Meta:
        model = Category


class SubCategoryFactory(factory.django.DjangoModelFactory):
    """ Generates dummy subcategory object """
    name = factory.Faker('word')
    parent_category = factory.iterator(Category.objects.all)

    class Meta:
        model = SubCategory


class AdvertisementFactory(factory.django.DjangoModelFactory):
    """ Generates dummy advertisement object """
    name = factory.Faker('sentence')
    owner = factory.iterator(User.objects.all)  # !TODO: If iterator is empty then creation crashes
    contact_email = factory.Faker('ascii_free_email')
    contact_phone = factory.Faker('phone_number')
    content = factory.Faker('text')
    views = factory.Faker('random_int')
    importance = factory.Faker('random_int')
    expires_date = factory.Faker('date_time_this_month')
    price = factory.Faker('random_int')
    location_city = factory.Faker('address')
    status = 'published'

    @factory.post_generation
    def subcategory(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            self.subcategory.add(factory.iterator(SubCategory.objects.all))

    class Meta:
        model = Advertisement


class AdvertisementImageFactory(factory.django.DjangoModelFactory):
    """ Generates dummy advertisement image object """
    description = factory.Faker('word')
    alternate_text = factory.Faker('word')
    parent_advertisement = factory.iterator(Advertisement.objects.all)
    image = factory.django.ImageField()

    class Meta:
        model = AdvertisementImage
