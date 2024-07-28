from django.db import models

# Salesperson Model
class Manager(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    start_date = models.DateField()
    termination_date = models.DateField(blank=True, null=True)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    
    class Meta:
        db_table = 'Manager'
        managed = False
        constraints = [
            models.UniqueConstraint(fields=['full_name','username'], name='U_Manager'),
        ]
        
    def __str__(self):
        return str(self.id)+": "+self.first_name+" "+self.last_name

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
        constraints = [
            models.UniqueConstraint(fields=['name'], name='U_Product') 
        ]
        
        
    def __str__(self):
        return str(self.id)+": "+self.name
        
# Salesperson Model
class Salesperson(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    start_date = models.DateField()
    termination_date = models.DateField(blank=True, null=True)
    manager_id = models.IntegerField()
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    
    class Meta:
        db_table = 'Salesperson'
        managed = False
        constraints = [
            models.UniqueConstraint(fields=['full_name','username'], name='U_Salesperson'),
        ]
        
    def __str__(self):
        return str(self.id)+": "+self.first_name+" "+self.last_name

# Customer Model
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

# Sale Model
class Sale(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.IntegerField()
    salesperson = models.IntegerField()
    customer = models.IntegerField()
    sale_date = models.DateField()
    
    class Meta:
        db_table = 'Sale'
        managed = False
    
# Discount Model
class Discount(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.IntegerField()
    begin_date = models.DateField()
    end_date = models.DateField()
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
   
    class Meta:
        db_table = 'Discount'
        managed = False
    

