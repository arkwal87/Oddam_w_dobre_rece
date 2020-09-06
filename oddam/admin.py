from django.contrib import admin
from .models import Donation, Category, Institution
from accounts.models import CustomUser

# Register your models here.

admin.site.register(Category)
admin.site.register(Donation)
admin.site.register(Institution)
admin.site.register(CustomUser)