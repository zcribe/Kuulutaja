import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_profile_view_get(client):
    url = reverse('profile')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_view_get(client):
    url = reverse('profile-email')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_view_get(client):
    url = reverse('profile-update')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_view_get(client):
    url = reverse('profile-password')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_view_get(client):
    url = reverse('profile-settings')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_view_get(client):
    url = reverse('profile-privacy')
    response = client.get(url)
    assert response.status_code == 200
