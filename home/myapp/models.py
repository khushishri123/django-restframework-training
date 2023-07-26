from django.db import models

# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name

class Employee(models.Model):
    name=models.CharField(max_length=50)
    dob=models.DateField()
    dept=models.ForeignKey(Department,on_delete=models.CASCADE,related_name="employee")
    salary=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self) -> str:
        return self.name