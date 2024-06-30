from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),



    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('create-room/',views.createRoom, name='create-room'),
    path('profile/<str:pk>/',views.userProfile, name='userProfile'),

    path('update-room/<str:pk>/',views.updatedRoom, name='update-room'),
    path('delete-room/<str:pk>/',views.deleteRoom, name='delete-room'),
    path('delete_meassage/<str:pk>/', views.delete_meassage, name='delete_meassage'),

    path('update-user/', views.updateUser, name='update-user'),
    path('topics/', views.topicsPage, name='topics'),
    path('activity/', views.activityPage, name='activity'),
]
