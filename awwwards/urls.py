from django.urls import path
from awwwards import views

urlpatterns = [
    path('',views.home,name='home'),
    path('post/',views.submitpost, name='post')
]