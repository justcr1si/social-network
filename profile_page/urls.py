from django.urls import path

from . import views

app_name = 'profile_page'

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('?user_id=<int:user_id>/', views.profile, name='profile'),
    path('', views.profile, name="profile"),
    path('image-handler/?user_id=<int:user_id>/', views.process_profile_photo,
         name='process-profile-photo'),
    path('description-handler/?user_id=<int:user_id>/',
         views.process_profile_description, name='process-profile-description'),
    path('detele-image-handler/?user_id=<int:user_id>/', views.delete_user_image,
         name='delete-image-handler'),
]
