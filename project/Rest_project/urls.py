from django.contrib import admin
from django.urls import path, include
from .views import RegisterCreateView, UserListView

urlpatterns = [
    path('api/v1/auth/register/', RegisterCreateView.as_view()),
    path('api/v1/user/', UserListView.as_view()),
]
