from django.shortcuts import render,HttpResponse,get_object_or_404
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework.status import HTTP_201_CREATED,HTTP_200_OK,HTTP_204_NO_CONTENT
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
# Create your views here.
def hello_world(request):
    return render(request,'hello.html')

@api_view(['GET','POST'])
def department_list(request):
    if request.method=="GET":
        queryset=Department.objects.all()
        serializer=DepartmentSerializer(queryset,many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer=DepartmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Added successfully",status=HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def department_details(request,id):
    department=get_object_or_404(Department,pk=id)
    if request.method=="GET":
        serializer=DepartmentSerializer(department)
        return Response(serializer.data)
    if request.method=="PUT":
        serializer=DepartmentSerializer(department,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Updated successfully",status=HTTP_200_OK)
    if request.method=="DELETE":
        if department.employee.count()>0:
            return Response({'error':'Cannot delete this departement as it is allocated to employees'})
    department.delete()
    return Response(status=HTTP_204_NO_CONTENT)
        
class EmployeeViewSet(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

