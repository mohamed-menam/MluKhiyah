from contextlib import nullcontext
from os import name
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Meal(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=360)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def no_rateing(self):
        rateing = Rateing.objects.filter(meal=self)
        return len(rateing)

    def averg_rateing(self):
        rateing = Rateing.objects.filter(meal=self)
        sum = 0
        for x in rateing:
            sum += x.stars
        if len(rateing) > 0:
            return len(rateing)/sum
        else:
            return 0

    def __str__(self):
        return self.title


class Rateing(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, blank=True, null=True)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'meal'),)
        index_together = (('user', 'meal'),)
