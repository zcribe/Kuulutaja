from django.core.management.base import BaseCommand, CommandError
from core.factories import CategoryFactory, SubCategoryFactory, AdvertisementFactory, AdvertisementImageFactory

CATEGORIES = 10
SUBCATEGORIES = 20
ADVERTISEMENTS = 500
ADVERTISEMENTS_IMAGES = 1000


class Command(BaseCommand):
    """ Creates dummy data for testing """
    help = "Generate testing data for the app"

    def handle(self, *args, **options):
        CategoryFactory.create_batch(size=CATEGORIES)
        self.stdout.write(self.style.SUCCESS(f'{CATEGORIES} categories generated'))
        SubCategoryFactory.create_batch(size=SUBCATEGORIES)
        self.stdout.write(self.style.SUCCESS(f'{SUBCATEGORIES} subcategories generated'))
        AdvertisementFactory.create_batch(size=ADVERTISEMENTS)
        self.stdout.write(self.style.SUCCESS(f'{ADVERTISEMENTS} advertisements generated'))
        AdvertisementImageFactory.create_batch(size=ADVERTISEMENTS_IMAGES)
        self.stdout.write(self.style.SUCCESS(f'{ADVERTISEMENTS_IMAGES} advertisement images generated'))
        self.stdout.write(self.style.SUCCESS('All test data generated successfully'))
