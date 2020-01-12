from datetime import datetime, timezone

import pytest
from django.urls import reverse

from core.models import Advertisement, Category


@pytest.mark.django_db
def test_index_view_get(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_search_view_get(client):
    url = reverse('search-results')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_category_view_get(client):
    Category.objects.create(
        name='test',
        depth='100'
    )
    url = reverse('category', {'slug': 'test-1'})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_detail_ad_view_get(client):
    Advertisement.objects.create(
        name='test',
        expires_date=datetime.now(timezone.utc).astimezone(),
        price=100.00,
        location_city='tallinn'
    )
    url = reverse('ad-detail', {'slug': 'test-1'})
    response = client.get(url)
    assert response.status_code == 200


