from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('goals/', views.goal_list, name='goal_list'),
    path('goals/create/', views.goal_create, name='goal_create'),
    path('goals/<int:goal_id>/tasks/', views.task_list, name='task_list'),
    path('goals/<int:goal_id>/tasks/new/', views.task_create, name='task_create'),
    path('goals/<int:goal_id>/tasks/<int:task_id>/complete/', views.complete_task, name='complete_task'),
    path('register/', views.register, name='register'),
    path('export_ics/', views.export_ics, name='export_ics'),
    path('accounts/profile/', views.profile_view, name='profile'),  # Profile URL
]
