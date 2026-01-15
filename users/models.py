from django.db import models
import datetime 


class Category(models.Model):
      name=models.CharField(max_length=300)


def __str__(self):
        return self.name


class Products(models.Model):
    name= models.CharField(max_length=100)
    slug = models.CharField(max_length=300, null=True, blank=True)  
    category= models.ForeignKey(Category,on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField(default=0)

def __str__(self):
        return self.name

class Customer(models.Model):
       first_name = models.CharField(max_length=50)
       last_name = models.CharField(max_length=50)
       phone = models.CharField(max_length=10)
       email = models.EmailField(unique=True)
       password = models.CharField(max_length=100)

def __str__(self):
    return self.first_name

class Review(models.Model):
      Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
      Products = models.ForeignKey(Products, on_delete=models.CASCADE)
      content = models.TextField()
      date = models.CharField(default=datetime.datetime.today)

def __str__(self):
    return self.Customer


class Order(models.Model):
      Products = models.ForeignKey(Products, on_delete=models.CASCADE)
      Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
      quantity = models.IntegerField(default=1)
      price = models.IntegerField()
      address = models.CharField(max_length=50, default='', blank=True)
      phone = models.CharField(max_length=50, default='', blank=True)
      date = models.CharField(default=datetime.datetime.today)
      status = models.BooleanField(default=False)

def __str__(self):
    return self.address


class CheckOutDetails(models.Model):
      Customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
      Order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
      phone_number = models.CharField(max_length=10,blank=True,null=True)
      total_amount = models.CharField(max_length=10,blank=True,null=True)
      address= models.CharField(max_length=300)
      city = models.CharField(max_length=100)
      state = models.CharField(max_length=100)
      zipcode = models.CharField(max_length=100)
      payment = models.CharField(max_length=100,blank=True)

def __str__(self):
    return self.address
