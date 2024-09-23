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
def test_create_new_task(api_client, create_task):
    #Generate URL for task view by name from urls.py
    url = reverse('tasks')
    data = {
        "title": "New Task",
        "description": "testing new task",
        "due_date": "2024-06-30",
        "status": "New"
    }
    response = api_client.post(url, data, format='json')
    print(response.data)
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_create_new_invalid_task(api_client, create_task):
    url = reverse('tasks')
    data = {}
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
