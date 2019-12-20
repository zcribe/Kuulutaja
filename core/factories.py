import random

import factory
from mimesis import Business, Address, Text, Person, Datetime, Internet

from .models import Category, SubCategory, Advertisement, AdvertisementImage

LOCALE = 'ee'

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
    parent_category = factory.iterator(Category.objects.all())

    class Meta:
        model = SubCategory


class AdvertisementFactory(factory.django.DjangoModelFactory):
    name = Text.title()
    owner = "user"
    contact_email = Person.email()
    contact_phone = Person.telephone()
    subcategory = factory.iterator(SubCategory.objects.all())
    content = Text.text(random.randint(3, 20))
    views = random.randint(0, 9000)
    importance = random.randint(0, 9000)
    expires_date = Datetime.datetime()
    price = Business.price()
    location_city = Address.city()
    users_interested = "user"

    class Meta:
        model = Advertisement


class AdvertisementImageFactory(factory.django.DjangoModelFactory):
    description = Text.title()
    alternate_text = Text.title()
    parent_advertisement = "advert"
    image = Internet.stock_image(500, 500, [description])

    class Meta:
        model = AdvertisementImage
