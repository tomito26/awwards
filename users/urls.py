from django.urls import path
from . import views
from .views import ListProfileView


urlpatterns = [
    path('api/profile/',ListProfileView.as_view())
]
