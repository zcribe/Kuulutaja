import factory
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Category, Advertisement, AdvertisementImage

LOCALE = 'et'
TIMEZONE = 'Europe/Tallinn'


def category_factory(size):
    """ Generates dummy category objects """
    count = 0

    root = Category.add_root(name='root_category')
    count += 1

    for _ in range(1, size):
        child = root.add_child(name=factory.Faker('word').generate().capitalize())
        count += 1
        for _ in range(1, size):
            child.add_child(name=factory.Faker('word').generate().capitalize())
            count += 1

    return count


class AdvertisementFactory(factory.django.DjangoModelFactory):
    """ Generates dummy advertisement object """
    name = factory.Faker('sentence')
    owner = factory.iterator(User.objects.all)  # !TODO: If iterator is empty then creation crashes
    category = factory.iterator(Category.objects.all)
    contact_email = factory.Faker('ascii_free_email')
    contact_phone = factory.Faker('phone_number')
    content = factory.Faker('text')
    views = factory.Faker('random_int')
    importance = factory.Faker('random_int')
    expires_date = factory.Faker('date_time_this_month', tzinfo=timezone.get_current_timezone())
    price = factory.Faker('random_int')
    location_city = factory.Faker('address')
    status = 'published'

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
