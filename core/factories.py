import random

import factory
from mimesis import Business, Address, Text, Person, Datetime, Internet
from django.contrib.auth.models import User

from .models import Category, SubCategory, Advertisement, AdvertisementImage

LOCALE = 'et'
TIMEZONE = 'Europe/Tallinn'

Business = Business(LOCALE)
Address = Address(LOCALE)
Text = Text(LOCALE)
Person = Person(LOCALE)
Datetime = Datetime(LOCALE)
Internet = Internet(LOCALE)


class CategoryFactory(factory.django.DjangoModelFactory):
    name = Text.title()

    class Meta:
        model = Category


class SubCategoryFactory(factory.django.DjangoModelFactory):
    name = Text.title()
    parent_category = factory.iterator(Category.objects.all)

    class Meta:
        model = SubCategory


class AdvertisementFactory(factory.django.DjangoModelFactory):
    name = Text.title()
    owner = factory.iterator(User.objects.all)
    contact_email = Person.email()
    contact_phone = Person.telephone()
    content = Text.text(random.randint(3, 20))
    views = random.randint(0, 9000)
    importance = random.randint(0, 9000)
    expires_date = Datetime.datetime(timezone=TIMEZONE)
    price = random.randint(1, 90000)
    location_city = Address.city()
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
    description = Text.title()
    alternate_text = Text.title()
    parent_advertisement = factory.iterator(Advertisement.objects.all)
    image = factory.django.ImageField()

    class Meta:
        model = AdvertisementImage
