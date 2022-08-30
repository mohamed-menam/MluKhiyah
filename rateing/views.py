from ast import Try

import imp
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurant, Meal, Rateing
from .serializers import RestaurantSerializer, MealSerializer, RateingSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.conf import settings


# Create your views here.


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def restaurant_list(request):
    if request.method == "GET":
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def restaurant_pk(request, pk):
    try:
        restaurant = Restaurant.objects.get(pk=pk)
    except Restaurant.DoesNotExist():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    if request.method == "PUT":
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    if request.method == "DELETE":
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def meal_list(request):
    if request.method == "GET":
        meals = Meal.objects.all()
        serializer = MealSerializer(meals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = MealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def meal_pk(request, pk):
    try:
        meal = Meal.objects.get(pk=pk)
    except Meal.DoesNotExist():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == "GET":
        serializer = MealSerializer(meal)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    if request.method == "PUT":
        serializer = MealSerializer(meal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "DELETE":
        meal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def rate_list(request):
    if request.method == "GET":
        rates = Rateing.objects.all()
        serializer = RateingSerializer(rates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = RateingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def rate_pk(request, pk):
    try:
        rate = Rateing.objects.get(pk=pk)
    except rate.DoesNotExist():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == "GET":
        serializer = RateingSerializer(rate)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    if request.method == "PUT":
        serializer = RateingSerializer(rate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "DELETE":
        rate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
@authentication_classes([TokenAuthentication, ])
@permission_classes([IsAuthenticated])
def create_list(request):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            massege = {
                "user": "user is created "
            }
            return Response(massege)
    else:
        massege = {
            "detail": "don't play here"
        }
        return Response()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
