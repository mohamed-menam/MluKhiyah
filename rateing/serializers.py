from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Restaurant, Meal, Rateing
from django.contrib.auth.models import User


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'title', 'description', 'restaurant',
                  'no_rateing', 'averg_rateing')


class RateingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rateing
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
