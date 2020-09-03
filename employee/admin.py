from django.contrib import admin
from .models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    raw_id_fields = ['company']
    search_fields = ('employee_name','salary')
    list_display = ('employee_name','salary')
admin.site.register(Employee,EmployeeAdmin)