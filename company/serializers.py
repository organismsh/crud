from rest_framework import serializers
from .models import (
    Company
)


class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('company_name', 'total_employees')