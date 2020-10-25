from django.db.models.query import Prefetch
from django.urls import path
from . import views
from .views import ProjectDeleteView, ProjectListView,ProjectDetailView,ProjectCreateView, ProjectUpdateView


urlpatterns = [
    path('',ProjectListView.as_view(),name='home'),
    path('project/<int:pk>/',ProjectDetailView.as_view(),name='project-detail'),
    path('project/new/',ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/update/',ProjectUpdateView.as_view(),name='project-update'),
    path('post/<int:pk>/delete',ProjectDeleteView.as_view(), name='project-delete')
]