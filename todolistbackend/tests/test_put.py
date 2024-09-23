import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from Tasks.models import Task

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_task():
    return Task.objects.create(
        title = "Test",
        description = "testing",
        due_date = "2024-06-30",
        status = "New Task"
    )

@pytest.mark.django_db
def test_update_task(api_client, create_task):
    url = reverse('task-item-detail', kwargs={'pk': create_task.pk})
    update_data = {
        "title": "Updated Task",
        "description": "updated description",
        "due_date": "2024-07-01",
        "status": "In Progress"
    }
    response = api_client.put(url, update_data, format='json')
    assert response.status_code == status.HTTP_200_OK

    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == "Updated Task"
    assert response.data['description'] == "updated description"
    assert response.data['due_date'] == "2024-07-01"
    assert response.data['status'] == "In Progress"



@pytest.mark.django_db
def test_update_fake_task(api_client):
    url = reverse('task-item-detail', kwargs={'pk': 1000})
    update_data = {
        "title": "Updated Task",
        "description": "updated description",
        "due_date": "2024-07-01",
        "status": "In Progress"
    }
    response = api_client.put(url, update_data, format='json')
    assert response.status_code == status.HTTP_404_NOT_FOUND


