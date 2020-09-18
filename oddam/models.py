from django.db import models
from accounts.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Institution(models.Model):
    INSTITUTION_TYPES = [
        ("FUN", "Fundacja"),
        ("ORG", "Organizacja Pozarządowa"),
        ("LOK", "Zbiórka lokalna")
    ]
    name = models.CharField(max_length=64)
    description = models.TextField()
    type = models.CharField(max_length=3, choices=INSTITUTION_TYPES, default="FUN")
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name + " - " + self.description


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=9)
    city = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.SET_NULL)
