from django.db import models

class Review(models.Model):

    score = models.IntegerField()
    comment = models.TextField()

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=240)
    image = models.ImageField()
    description = models.TextField(max_length=500)
    reviews = models.ManyToManyField(Review, related_name="reviews")
    price = models.FloatField()
