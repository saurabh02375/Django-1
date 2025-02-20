

from django.contrib import admin
from django.urls import path
from front import views
urlpatterns = [
    path("", views.index , name='index'),
     path("aboutus", views.aboutus , name='aboutus'),
  
]
