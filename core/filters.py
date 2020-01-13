import django_filters

from .models import Advertisement


class AdvertFilter(django_filters.FilterSet):
    class Meta:
        model = Advertisement
        fields = ['name', 'category', 'views', 'importance', 'expires_date', 'published_date', 'location_city']
