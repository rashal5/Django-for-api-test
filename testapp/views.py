from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializer import EmployeeSerializer

@api_view(['GET'])
def all_employee(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def all_check(request,id):
    employee = Employee.objects.get(id=id)
    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def all_delete(request,id):
    employee = Employee.objects.get(id=id) 
    employee.delete()
    return Response('employee deleted')

@api_view(['POST'])
def employee_create(request):
    print(request.data)
    employee_obj = Employee()
    employee_obj.first_name = request.data.get('first_name')
    employee_obj.last_name = request.data.get('last_name')
    employee_obj.email = request.data.get('email')
    employee_obj.phone_number = request.data.get('phone_number')
    employee_obj.save()
    return Response('employee data added') 


@api_view(['POST'])
def employee_createuseingser(request):
    print(request.data)
    serial = EmployeeSerializer(data=request.data)
    if serial.is_valid():
        serial.save()
        return Response("data kitty")
    return Response(serial.errors)
        

@api_view(['PUT'])
def employee_update(request,id):
    employee = Employee.objects.get(id=id)
    serial = EmployeeSerializer(instance=employee, data=request.data, partial=True)
    if serial.is_valid():
        serial.save()
        return Response("data update chyth")
    return Response(serial.errors)
        