from django.urls import path
from .import views

urlpatterns = [
    path('create', views.add_employee, name='add_employee'),
    path('all_employee/<int:id>', views.all_employee, name='all_employee'),
]
