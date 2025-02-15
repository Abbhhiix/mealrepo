from django.db import models
from django.contrib.auth.models import User

class UserBudget(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    budget = models.FloatField()
    dietary_preference = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.budget} - {self.dietary_preference}"

#budget constarints
class UserBudget(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    budget = models.FloatField()
    dietary_preference = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username}'s budget"
#recipe
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    cost = models.FloatField()
    dietary_preference = models.CharField(max_length=50)

    def __str__(self):
        return self.name
