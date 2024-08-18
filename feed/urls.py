from django.urls import path, include

from . import views

app_name = 'feed'

urlpatterns = [
    path('?user_id=<int:user_id>', views.display_feed, name='feed'),
    path('create-post/?user_id=<int:user_id>',
         views.create_post, name='create-post'),
    path('edit-post/?post_id=<int:post_id>&user_id=<int:user_id>/',
         views.edit_post, name='edit-post'),
    path('edit-post/?post_id=<int:post_id>/',
         views.edit_post, name='edit-post'),
    path('delete-post/?post_id=<int:post_id>',
         views.delete_post, name='delete-post'),
    path('', views.display_feed, name='feed'),
]
