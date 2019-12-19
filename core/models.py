from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db.models import PointField
from django.utils.text import slugify

"""
 Abstract models
 """


class TimeStamped(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModel(TimeStamped):
    name = models.TextField(null=False)
    slug = models.SlugField(default="", editable=False, unique=True)
    draft = models.BooleanField(default=True, null=False)
    published = models.BooleanField(default=False, null=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    """
     Autogenerates slug field
     """

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(BaseModel, self).save(*args, **kwargs)


"""
 Actual DB models
 """


class Category(BaseModel):
    """
     The main category for organisationl purposes
     """
    pass


class SubCategory(BaseModel):
    """
     Subcategory for organisationl purposes
     """
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')


class Advertisement(BaseModel):
    """
    The core advertisement an user creates
    """
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='subcategory')
    content = models.TextField(null=False)
    views = models.IntegerField(auto_created=True, default=0, null=False)
    importance = models.IntegerField(auto_created=True, default=0, null=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    contact_email = models.EmailField(null=False)
    expires_date = models.DateTimeField()
    expired = models.BooleanField(default=False, null=False)
    price = models.DecimalField()
    location_coordinate = PointField()
    location_city = models.TextField()
    contact_phone = models.IntegerField()


class AdvertisementImage(TimeStamped):
    """ Single image on advertisement"""
    description = models.TextField(default="")
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='advertisement')
    image = models.ImageField(null=False)
    alternate_text = models.CharField(default="", )
