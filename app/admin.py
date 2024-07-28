from django.contrib import admin
from .models import Product, Salesperson, Customer, Sale, Discount, Manager

#Admin register for Manager
@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'address', 'phone',
                    'start_date', 'termination_date', 'username', 'password')
    
#Admin register for Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manufacturer', 'style', 'purchase_price', 
                    'sale_price', 'quantity_on_hand', 'commision_percentage')
   
#Admin register for Salesperson 
@admin.register(Salesperson)
class SalespersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'address', 'phone',
                    'start_date', 'termination_date', 'manager_id', 'username', 'password')
  
#Admin register for Customer  
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'address', 'phone', 'start_date')
  
#Admin register for Sale  
@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'salesperson', 'customer', 'sale_date')
  
#Admin regisre for Discount  
@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'begin_date', 'end_date', 'discount_percentage')
    