from django.db import models

# Create your models here.
class MenuItems(models.Model):
    item_name = models.CharField(max_length=200)
    category = models.CharField(max_length=300)
    year = models.IntegerField()
    course = models.CharField(max_length=300)
