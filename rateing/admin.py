from django.contrib import admin
from .models import Restaurant, Meal, Rateing


# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'place']


class MealAdmin(admin.ModelAdmin):
    list_display = ['title', 'restaurant']
    search_fields = ['title']
    list_filter = ['title', 'restaurant']


class RateingAdmin(admin.ModelAdmin):
    list_display = ['meal', 'restaurant', 'stars']
    list_filter = ['meal', 'restaurant']


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(Rateing, RateingAdmin)
