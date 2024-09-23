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
def test_get_all_tasks(api_client, create_task):
    #Generate URL for task view by name from urls.py
    url = reverse('tasks')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['title'] == "Test"

@pytest.mark.django_db
def test_get_single_task(api_client, create_task): 
    url = reverse('task-item-detail', kwargs={'pk': create_task.pk})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == create_task.title

@pytest.mark.django_db
def test_get_fake_task(api_client):
    url = reverse('task-item-detail', kwargs={'pk': 1012039123})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_get_all_0_tasks(api_client):
    url = reverse('tasks')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 0