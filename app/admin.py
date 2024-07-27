from django.contrib import admin
from .models import TestTable

# Register your models here.

@admin.register(TestTable)
class TestTableAdmin(admin.ModelAdmin):
    list_display = ('ID', "Name")