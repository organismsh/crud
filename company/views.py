from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from .serializers import (
    CompanyCreateSerializer
)
from .models import (
    Company
)

@api_view(['POST'])
def add_company(request):
    serializer = CompanyCreateSerializer(data=request.data)
    if serializer.is_valid():
        company = serializer.save()
        if company:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
url : /company/all_companies 
url with search params: /company/all_companies?search=company name
url with pagination /company/all_companies?page=1
url with pagination and search /company/all_companies?page=1&search=2

Returns 10 objects on a request along with next and previous pagination links with count

for the search part query need to be passed ?search=value which is optional
"""
@api_view(['GET'])
def all_companies(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10

    search = request.query_params.get('search', None)

    if search is not None:
        companies = Company.objects.filter(Q(company_name__icontains=search))
    else:
        companies = Company.objects.all()

    result_page = paginator.paginate_queryset(companies, request)
    serializer = CompanyCreateSerializer(result_page,many=True)
    if serializer:
        return paginator.get_paginated_response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def company(request,id):
    company_obj = Company.objects.filter(id=id)
    if not company_obj.exists():
        return Response({"response":"not_found"}, status=status.HTTP_400_BAD_REQUEST)
    serializer = CompanyCreateSerializer(company_obj.first())
    if serializer:
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
