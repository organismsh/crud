from django.contrib import admin
from .models import Company
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    search_fields = ('company_name',)
    list_display = ('company_name','total_employees')
admin.site.register(Company,CompanyAdmin)