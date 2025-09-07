from django.db import models
import uuid
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length= 50)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length = 50)
    is_featured = models.BooleanField(default = False)
    stock = models.IntegerField()
    rating = models.IntegerField()
