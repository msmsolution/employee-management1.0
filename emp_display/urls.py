from django.contrib import admin
from django.urls import path,include
from emp_display import views

urlpatterns = [
    path("employee/",views.emp_details),
]
