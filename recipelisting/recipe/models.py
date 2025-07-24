from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description= models.TextField(default='No description provided')
    ingredients = models.TextField(default = 'Unknown ingredients')
    steps = models.TextField(default = 'No steps provided')

    def __str__(self):
        return self.title