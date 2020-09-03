from django.db import models
from company.models import Company
from django.db.models.signals import post_save
from django.dispatch import receiver

class Employee(models.Model):
    employee_name = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,related_name="employee")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


"""
using signal to add the total employee count to the company to avoid direct count queries for each request on company get request
"""
@receiver(post_save, sender=Employee)
def company_employee_count(sender,instance,created, **kwargs):
    if created:
        instance.company.total_employees = Employee.objects.filter(company=instance.company).count()
        instance.company.save()