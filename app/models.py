from django.db import models

# Product Model
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    purchase_price = models.DecimalField(max_digits=8, decimal_places=2)
    sale_price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity_on_hand = models.IntegerField()
    commision_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'Product'
        managed = False
        
    def __str__(self):
        return str(self.id)+": "+self.name
        
# Salesperson Model
class Salesperson(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    start_date = models.DateField()
    termination_date = models.DateField(blank=True, null=True)
    manager = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'Salesperson'
        managed = False
        
    def __str__(self):
        return str(self.id)+": "+self.first_name+" "+self.last_name

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    start_date = models.DateField()
    
    class Meta:
        db_table = 'Customer'
        managed = False
        
    def __str__(self):
        return str(self.id)+": "+self.first_name+" "+self.last_name

class Sale(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sale_date = models.DateField()
    
class Discount(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
   
    
    

