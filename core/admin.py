from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvertisementImage)
class AdvertisementImageAdmin(admin.ModelAdmin):
    pass
