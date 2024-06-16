from django.contrib import admin
from . import models

@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand','model', 'price']

@admin.register(models.Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'display_brands', 'new_or_used']
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name'] 
    

    def display_brands(self, obj):
        return ", ".join([brand.brand for brand in obj.brand.all()])




@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['brand']

@admin.register(models.Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model']
 

    
