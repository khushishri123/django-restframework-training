from .models import *
from rest_framework import serializers
from .models import *

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=['name']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=['id','name','dob','dept','salary','annualSalary']
    annualSalary=serializers.SerializerMethodField(method_name='findAnnualSalary')
    def findAnnualSalary(self,employee:Employee):
        return 12*employee.salary

