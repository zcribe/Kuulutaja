from io import BytesIO

from django.db import models
from django.conf import settings
from django.utils.text import slugify
from taggit.managers import TaggableManager
from PIL import Image

from .constants import MAX_ALT_LENGTH, PRICE_MAX_DECIMALS, PRICE_MAX_DIGITS, IMAGE_COMPRESSION_FORMAT, \
    IMAGE_COMPRESSION_QUALITY


class TimeStamped(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModel(TimeStamped):
    name = models.CharField(null=False, max_length=150)
    slug = models.SlugField(default="", editable=False, unique=True)
    draft = models.BooleanField(default=True, null=False)
    published = models.BooleanField(default=False, null=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Auto generates slug field"""
        self.slug = slugify(self.name)
        super(BaseModel, self).save(*args, **kwargs)


class Category(BaseModel):
    """The main category for organisationl purposes"""
    pass

    class Meta:
        verbose_name_plural = 'Categories'


class SubCategory(BaseModel):
    """Subcategory for organisationl purposes"""
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    class Meta:
        verbose_name_plural = 'Sub categories'


class Advertisement(BaseModel):
    """The core advertisement an user creates"""
    expired = models.BooleanField(default=False, null=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact_email = models.EmailField(null=False)
    contact_phone = models.IntegerField()
    subcategory = models.ManyToManyField(SubCategory, related_name='subcategory')
    content = models.TextField(null=False)
    views = models.IntegerField(auto_created=True, default=0, null=False, editable=False)
    importance = models.IntegerField(auto_created=True, default=0, null=False)
    expires_date = models.DateTimeField()
    price = models.DecimalField(decimal_places=PRICE_MAX_DECIMALS, max_digits=PRICE_MAX_DIGITS)
    location_city = models.CharField(max_length=100)
    users_interested = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='users_interested', blank=True)
    tags = TaggableManager()

    class Meta:
        ordering = ['-created_date']


class AdvertisementImage(TimeStamped):
    """ Single image on advertisement"""
    description = models.CharField(default="", max_length=150)
    alternate_text = models.CharField(default="", max_length=MAX_ALT_LENGTH)
    parent_advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='advertisement')
    image = models.ImageField(null=False)

    def save(self, *args, **kwargs):
        """ Compress image on save"""
        input_image = Image.open(self.image)
        output_image = BytesIO()
        input_image.save(output_image, format=IMAGE_COMPRESSION_FORMAT, quality=IMAGE_COMPRESSION_QUALITY)
        super(AdvertisementImage, self).save(*args, **kwargs)


class PublishedAdvertisementsManager(models.Manager):
    def get_queryset(self):
        return super(PublishedAdvertisementsManager, self).get_queryset().filter(status='published')
