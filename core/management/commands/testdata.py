from django.core.management.base import BaseCommand, CommandError
from core.factories import category_factory, AdvertisementFactory, AdvertisementImageFactory

CATEGORIES = 10
ADVERTISEMENTS = 500
ADVERTISEMENTS_IMAGES = 1000


class Command(BaseCommand):
    """ Creates dummy data for testing """
    help = "Generate testing data for the app"

    def handle(self, *args, **options):
        cats = category_factory(size=CATEGORIES)
        self.stdout.write(self.style.SUCCESS(f'{cats} categories generated'))
        AdvertisementFactory.create_batch(size=ADVERTISEMENTS)
        self.stdout.write(self.style.SUCCESS(f'{ADVERTISEMENTS} advertisements generated'))
        AdvertisementImageFactory.create_batch(size=ADVERTISEMENTS_IMAGES)
        self.stdout.write(self.style.SUCCESS(f'{ADVERTISEMENTS_IMAGES} advertisement images generated'))
        self.stdout.write(self.style.SUCCESS('All test data generated successfully'))
