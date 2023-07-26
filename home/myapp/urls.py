
from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import SimpleRouter

router=SimpleRouter()
router.register('employee',views.EmployeeViewSet)

urlpatterns = [
    path('hello/',views.hello_world,name="hello"),
    path('departmentList/',views.department_list,name="departmentList"),
    path('departmentDetails/<int:id>',views.department_details,name="departmentDetails"),
    path('',include(router.urls))

]
