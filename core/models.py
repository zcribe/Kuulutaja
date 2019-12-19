from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db.models import PointField


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=True, null=False)
    published = models.BooleanField(default=False, null=False)

    class Meta:
        abstract = True


class Category(BaseModel):
    """ The main category for organisationl purposes"""
    title = models.TextField(null=False)


class SubCategory(BaseModel):
    """ Subcategory for organisationl purposes"""
    title = models.TextField(null=False)
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Advertisement(BaseModel):
    """ The core advertisement an user creates"""
    title = models.TextField(null=False)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    content = models.TextField(null=False)
    views = models.IntegerField(auto_created=True, default=0, null=False)
    importance = models.IntegerField(auto_created=True, default=0, null=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    contact_email = models.EmailField(null=False)
    price = models.DecimalField()
    location_coordinate = PointField()
    location_city = models.TextField()
    contact_phone = models.IntegerField()

