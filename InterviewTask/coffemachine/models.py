# Create your models here.
from django.db import models
from django.utils import timezone


All_Product_Types = [
    ("COFFEE_MACHINE_LARGE", "COFFEE_MACHINE_LARGE"),
    ("COFFEE_MACHINE_SMALL", "COFFEE_MACHINE_SMALL"),
    ("ESPRESSO_MACHINE", "ESPRESSO_MACHINE"),
]

class CoffeMachine(models.Model):
    date_created = models.DateTimeField(default=timezone.now)
    product_type = models.CharField(max_length=60, choices=All_Product_Types)
    name = models.CharField(max_length=60)
    water_line_compatible=models.BooleanField(default=True)
    def __str__(self):
        return self.name
  
