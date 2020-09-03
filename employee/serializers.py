from rest_framework import serializers
from company.serializers import (
    CompanyCreateSerializer
)
from .models import (
    Employee
)


class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('employee_name', 'salary','company')