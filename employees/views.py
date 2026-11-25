from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee
from rest_framework . decorators import api_view
from rest_framework . response import Response
from . serializer import EmployeeSerializer
from rest_framework import status 
# Create your views here.
@api_view(['GET'])
def employ(request):
    nk=Employee.objects.all()
    rp=EmployeeSerializer(nk,many=True)
    return Response(rp.data,status=status.HTTP_200_OK)

