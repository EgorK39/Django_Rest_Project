from rest_framework import serializers
from .models import RegisterView


class RegisterCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterView
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterView
        fields = (
            'id',
            'phone',
            'login',
            'name',
            'birth',
            'tg',
            'email',
        )
