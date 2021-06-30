from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects_home, name='projects_home'),
    path('create', views.create, name='create'),
    path('create_task', views.create_task, name='create_task'),
    path('<int:pk>', views.ProjectsDetailView.as_view(), name='projects-detail'),
    path('<int:pk>/update_task', views.TasksUpdateView.as_view(), name='tasks-update'),
    path('<int:pk>/delete_task', views.TasksDeleteView.as_view(), name='tasks-delete'),
    path('<int:pk>/update', views.ProjectsUpdateView.as_view(), name='projects-update'),
    path('<int:pk>/delete', views.ProjectsDeleteView.as_view(), name='projects-delete'),
]