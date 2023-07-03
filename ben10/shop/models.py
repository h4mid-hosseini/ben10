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


class Invoice(TimeStampedModel):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.PositiveBigIntegerField(blank=True, null=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}"


class InvoiceItem(TimeStampedModel):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveBigIntegerField()

    def get_cost(self):
        return self.price * self.quantity
