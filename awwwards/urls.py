from django.db.models.query import Prefetch
from django.urls import path,re_path
from . import views
from .views import ListProjectsView, ProjectDeleteView, ProjectListView,ProjectDetailView,ProjectCreateView, ProjectUpdateView, UserProjectListView


urlpatterns = [
    path('',ProjectListView.as_view(),name='home'),
    path('user/<str:username>/',UserProjectListView.as_view(),name='user-projects'),
    path('project/<int:pk>/',ProjectDetailView.as_view(),name='project-detail'),
    path('project/new/',ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/update/',ProjectUpdateView.as_view(),name='project-update'),
    path('project/<int:pk>/delete',ProjectDeleteView.as_view(), name='project-delete'),
    path('search/',views.search_results, name='search_results'),
    path('project/<int:project_id>/rate',views.rate,name='rate-movie'),
    re_path('api/project/', ListProjectsView.as_view())
        
]