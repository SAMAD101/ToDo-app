from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_task/', views.add_task, name='add_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('mark_complete/<int:task_id>/', views.mark_complete, name='mark_complete'),
    path('completed_tasks/', views.completed_tasks, name='completed_tasks'),
    path('mark_incomplete/<int:task_id>/', views.mark_incomplete, name='mark_incomplete'),
]