from django.contrib import admin
from .models import Category
from .models import Products
from .models import Customer
from .models import Order
from .models import Review
from .models import CheckOutDetails

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(CheckOutDetails)