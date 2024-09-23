from django.urls import path
from . import views


urlpatterns = [
    path('tasks/', views.TaskFeedView.as_view(), name='tasks'),
    path('tasks/<int:pk>', views.TaskFeedView.as_view(), name='task-item-detail')
]