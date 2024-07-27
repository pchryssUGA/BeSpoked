from django.contrib import admin
from .models import Product, Salesperson, Customer, Sale, Discount

# Register your models here.
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manufacturer', 'style', 'purchase_price', 
                    'sale_price', 'quantity_on_hand', 'commision_percentage')
    
@admin.register(Salesperson)
class SalespersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'address', 'phone',
                    'start_date', 'termination_date', 'manager')
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'address', 'phone', 'start_date')
    
@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'salesperson', 'customer', 'sale_date')
    
@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'start_date', 'end_date', 'discount_percentage')
    