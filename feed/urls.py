from django.urls import path

from . import views

app_name = 'feed'

urlpatterns = [
    path('', views.display_feed, name='feed'),
    path('create-post/?user_id=<int:user_id>', views.create_post, name='create-post'),
]
