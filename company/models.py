from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    total_employees = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


