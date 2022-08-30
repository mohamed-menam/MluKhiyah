from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('restaurant_list/', views.restaurant_list),
    path("restaurant_pk/<int:pk>", views.restaurant_pk),
    path("meal_list/", views.meal_list),
    path("meal_pk/<int:pk>", views.meal_pk),
    path("rate_list/", views.rate_list),
    path("rate_pk/<int:pk>", views.rate_pk),
    path('create_list/', views.create_list),
    path('tokenrequest/', obtain_auth_token)

]
