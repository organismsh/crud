from django.urls import path
from .import views

urlpatterns = [
    path('create', views.add_company, name='add_company'),
    path('all_companies', views.all_companies, name='all_companies'),
    path('<int:id>', views.company, name='company')
]
