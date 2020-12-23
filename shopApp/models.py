from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class  Customer(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    phone = models.CharField(max_length=16)
    city = models.CharField(max_length=20)
    def __str__(self):
        return self.firstName+' '+self.lastName

class Order(models.Model):
    product = models.CharField(max_length=40)
    price = models.IntegerField()
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer, related_name="orders", on_delete=models.CASCADE)
    def __str__(self):
        return self.product+' '+self.price
