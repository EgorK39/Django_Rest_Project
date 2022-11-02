from django.shortcuts import render
from rest_framework import generics
from .serializers import RegisterCreateSerializer, UserListSerializer
from .models import RegisterView


# Create your views here.

class RegisterCreateView(generics.CreateAPIView):
    serializer_class = RegisterCreateSerializer
    # permission_classes = ...


class UserListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = RegisterView.objects.all()
