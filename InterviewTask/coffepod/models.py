# Create your models here.
from django.db import models
from django.utils import timezone


All_Product_Types = [
    ("COFFEE_POD_LARGE", "COFFEE_POD_LARGE"),
    ("COFFEE_POD_SMALL", "COFFEE_POD_SMALL"),
    ("ESPRESSO_POD", "ESPRESSO_POD"),
]

All_Flavor_Types = [
    ("COFFEE_FLAVOR_VANILLA", "COFFEE_FLAVOR_VANILLA"),
    ("COFFEE_FLAVOR_CARAMEL", "COFFEE_FLAVOR_CARAMEL"),
    ("COFFEE_FLAVOR_PSL", "COFFEE_FLAVOR_PSL"),
    ("COFFEE_FLAVOR_MOCHA", "COFFEE_FLAVOR_MOCHA"),
    ("COFFEE_FLAVOR_HAZELNUT", "COFFEE_FLAVOR_HAZELNUT"),
]
All_Sizes_Types = [
    ("1", "1"),
    ("3", "3"),
    ("5", "5"),
    ("7", "7"),
]
class CoffePod(models.Model):
    date_created = models.DateTimeField(default=timezone.now)
    product_type = models.CharField(max_length=60, choices=All_Product_Types)
    flavor_type = models.CharField(max_length=60, choices=All_Flavor_Types)
    size_type = models.CharField(max_length=60, choices=All_Sizes_Types)
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name
  
