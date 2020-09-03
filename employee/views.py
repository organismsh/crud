from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from .serializers import (
    EmployeeCreateSerializer
)
from .models import (
    Employee
)


@api_view(['POST'])
def add_employee(request):
    serializer = EmployeeCreateSerializer(data=request.data)
    if serializer.is_valid():
        employee = serializer.save()
        if employee:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



"""
url : employee/all_employee/<company_id> 
url with search params: employee/all_employee/<company_id>?search=employee name
url with search params: employee/all_employee/<company_id>?salary_range=1000
url with pagination employee/all_employee/<company_id>?page=1
url with pagination and search employee/all_employee/<company_id>?page=1&search=employee name

Returns 10 objects on a request along with next and previous pagination links with count

for the search part query need to be passed ?search=value which is optional
for the salary range part query need to be passed ?salary_range=1000 which is optional
"""
@api_view(['GET'])
def all_employee(request,id):
    paginator = PageNumberPagination()
    paginator.page_size = 10

    search = request.query_params.get('search', None)
    salary_range = request.query_params.get('salary_range', None)
    
    employee = Employee.objects.filter(company__id=id)

    if search is not None:
        employee = employee.filter(Q(employee_name__icontains=search))
    
    if salary_range is not None:
        employee = employee.filter(salary__range=(0,salary_range))

    result_page = paginator.paginate_queryset(employee, request)
    serializer = EmployeeCreateSerializer(result_page,many=True)
    if serializer:
        return paginator.get_paginated_response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)