

from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("", views.index , name='home'),
    path("about", views.about , name='about'),
    path("post", views.post , name='post'),
    path("create-post", views.addpost , name='addpost'),
    path("savepost", views.savepost , name='savepost'),
    path('deletepost/<int:post_id>/', views.delete_post, name='delete_post'),
    path('edit-post/<int:post_id>/', views.editpost, name='editpost'),
    path("home", views.home , name='home'),
]
