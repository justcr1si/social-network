from django.urls import path, include

from . import views

app_name = 'comments'

urlpatterns = [
    path('?post_id=<int:post_id>/', views.view_comments, name='view-comments'),
    path('leave-comments/?post_id=<int:post_id>&user_id=<int:user_id>',
         views.leave_comment, name='leave-comment'),
]
