from io import BytesIO

from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.db import IntegrityError
from taggit.managers import TaggableManager
from PIL import Image
from model_utils.models import StatusModel, TimeStampedModel, SoftDeletableModel
from model_utils import Choices
from model_utils.managers import QueryManager

from phonenumber_field.modelfields import PhoneNumberField

from .constants import MAX_ALT_LENGTH, PRICE_MAX_DECIMALS, PRICE_MAX_DIGITS, IMAGE_COMPRESSION_FORMAT, \
    IMAGE_COMPRESSION_QUALITY, NAME_MAX_LENGTH, SLUG_MAX_LENGTH,  CITY_MAX_LENGTH, \
    AD_DESCRIPTION_MAX_LENGTH


class BaseModel(TimeStampedModel, StatusModel, SoftDeletableModel):
    """ Abstract core model for every class """
    STATUS = Choices('draft', 'published', 'expired')
    name = models.CharField(null=False, max_length=NAME_MAX_LENGTH)
    slug = models.SlugField(default="", unique=True, max_length=SLUG_MAX_LENGTH)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Auto generates slug field"""
        try:
            slug_prototype = slugify(self.name)
            if len(slug_prototype) >= SLUG_MAX_LENGTH:
                self.slug = slug_prototype[0:SLUG_MAX_LENGTH]
            else:
                self.slug = slug_prototype

            super(BaseModel, self).save(*args, **kwargs)
        except IntegrityError as e:
            if 'unique constrain' in e.args:
                slug = f"{self.name}{self.pk}"
                slug_prototype = slugify(slug)
                if len(slug_prototype) >= SLUG_MAX_LENGTH:
                    self.slug = slug_prototype[0:SLUG_MAX_LENGTH]
                else:
                    self.slug = slug_prototype
                super(BaseModel, self).save(*args, **kwargs)


class Category(BaseModel):
    """The main category for organisationl purposes"""

    class Meta:
        verbose_name_plural = 'Categories'


class SubCategory(BaseModel):
    """Subcategory for organisationl purposes"""
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    class Meta:
        verbose_name_plural = 'Sub categories'


class Advertisement(BaseModel):
    """The core advertisement an user creates"""
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact_email = models.EmailField(null=False)
    contact_phone = PhoneNumberField(blank=True)
    subcategory = models.ManyToManyField(SubCategory, related_name='subcategory')
    content = models.TextField(null=False)
    views = models.IntegerField(auto_created=True, default=0, null=False, editable=False)
    importance = models.IntegerField(auto_created=True, default=0, null=False)
    expires_date = models.DateTimeField()
    price = models.DecimalField(decimal_places=PRICE_MAX_DECIMALS, max_digits=PRICE_MAX_DIGITS)
    location_city = models.CharField(max_length=CITY_MAX_LENGTH)
    users_interested = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='users_interested', blank=True)
    published_date = models.DateTimeField(blank=True, null=True)

    tags = TaggableManager()
    objects = models.Manager()
    public = QueryManager(published=True, is_removed=False).order_by('-published_date')

    class Meta:
        ordering = ['-created']


class AdvertisementImage(TimeStampedModel):
    """ Single image on advertisement"""
    description = models.CharField(default="", max_length=AD_DESCRIPTION_MAX_LENGTH)
    alternate_text = models.CharField(default="", max_length=MAX_ALT_LENGTH)
    parent_advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='advertisement')
    image = models.ImageField(null=False, upload_to='ads/')

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        """ Compress image on save"""
        input_image = Image.open(self.image)
        output_image = BytesIO()
        input_image.save(output_image, format=IMAGE_COMPRESSION_FORMAT, quality=IMAGE_COMPRESSION_QUALITY)
        super(AdvertisementImage, self).save(*args, **kwargs)
