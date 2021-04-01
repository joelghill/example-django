from django.db import models

# Create your models here.
class car(models.Model):
    name = models.TextField(max_length=120)