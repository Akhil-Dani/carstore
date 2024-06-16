from django.conf import settings
from django.contrib import admin
from django.db import models
from django.core.validators import MinValueValidator



class Brand(models.Model):
    brand = models.CharField(max_length=55)

    def __str__(self):
        return self.brand

class Model(models.Model):
    model = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE)

    def __str__(self):
        return self.model


   
class Car(models.Model):
    NEW = 'N'
    USED = 'U'

    neworused_choice = [
        (NEW , 'new'),
        (USED , 'used'),
    ]

    PETROL = 'P'
    DIESEL = 'D'
    ELECTRIC = 'E'

    FUEL_TYPE = [
        (PETROL , 'petrol'),
        (DIESEL , 'diesel'),
        (ELECTRIC, 'electric')

    ]

    new_or_used = models.CharField(max_length=1,
                                   choices = neworused_choice)
    price = models.IntegerField(validators=[MinValueValidator(1)])
    last_update = models.DateTimeField(auto_now=True)
    fuel_type = models.CharField(max_length=1, choices=FUEL_TYPE)
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
    model = models.ForeignKey(Model, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
 
    
class Buyer(models.Model):

    NEW = 'N'
    USED = 'U'

    neworused_choice = [
        (NEW , 'new'),
        (USED , 'used'),
    ]
   
    phone = models.CharField(max_length=255)
    brand = models.ManyToManyField(Brand)
    new_or_used = models.CharField(max_length=1,
                                   choices = neworused_choice)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name }'
    
    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name
    
    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name
    
    class Meta:
        ordering = ['user__first_name', 'user__last_name']

class Deal(models.Model):
    
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETE = 'C'
    PAYMENT_FAILED = 'F'

    PAYMENT_CHOICES = [
        (PAYMENT_PENDING, 'Pending'),
        (PAYMENT_COMPLETE, 'Complete'),
        (PAYMENT_FAILED, 'Failed'),
    ]
    
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_CHOICES, default=PAYMENT_PENDING)

