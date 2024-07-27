from django.db import models

# Create your models here.
class TestTable(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=10)
    
    class Meta:
        db_table = 'test_table'
        managed = False
    
