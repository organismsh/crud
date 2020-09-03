from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Company

class CompanyTest(APITestCase):
    def test_positive_company_create(self):

        url = reverse('add_company')
        data = {'company_name': 'Test Company'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 1)
        self.assertEqual(Company.objects.get().company_name, 'Test Company')
    
    def test_negative_company_create(self):

        url = reverse('add_company')
        data = {}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)