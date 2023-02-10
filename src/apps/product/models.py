from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=63)
    description = models.TextField()
    price = models.FloatField(validators=[MinValueValidator(0.1)])
    currency = models.ForeignKey("Currency", on_delete=models.PROTECT)


class Order(models.Model):
    items = models.ManyToManyField(Item)
    discount = models.ForeignKey("Discount", on_delete=models.PROTECT, null=True)
    tax = models.ForeignKey("Tax", on_delete=models.PROTECT)


class Discount(models.Model):
    discount_percentage = models.IntegerField(
        validators=[MinValueValidator(1)], unique=True
    )


class Tax(models.Model):
    tax_name = models.CharField(max_length=63)
    tax_percentage = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)]
    )


class Currency(models.Model):
    currency_name = models.CharField(max_length=10)

    def __str__(self):
        return self.currency_name.upper()
