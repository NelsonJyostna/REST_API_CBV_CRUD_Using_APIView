from django.shortcuts import render
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

from rest_framework import status
from rest_framework.views import APIView


# Create your views here.
class EmployeeAPI(APIView):
    def get(self, request, pk=None):
        id = pk
        if id is not None:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)  
            return Response(serializer.data)
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response({'msg':'Employee Register'}, status=status.HTTP_201_CREATED)
        else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        id = pk
        emp = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(emp, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Update completed'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        id= pk
        # id=id
        emp = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(emp, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial data completed'})
        else:
            return Response(serializer.errors)    

    def delete(self, request, pk):
        id=pk
        emp=Employee.objects.get(id=pk)
        emp.delete()
        return Response({'msg':'Data Deleted'})        