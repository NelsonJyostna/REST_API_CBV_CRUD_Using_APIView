from django.urls import path
from . import views

urlpatterns=[
    path('emp/', views.EmployeeAPI.as_view()),

    path('emp/<int:pk>/', views.EmployeeAPI.as_view()),
]