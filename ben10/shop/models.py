from django.db import models
from core.models import TimeStampedModel
from django.contrib.auth.models import User


# Create your models here.

class Product(TimeStampedModel):
    """ Product Model """
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    price = models.BigIntegerField()
    number = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
