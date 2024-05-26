from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from emp.models import Emp

# Fetch all users from the database
users = User.objects.all()

# Fetch all employees from the database
emps = Emp.objects.all()

# Compare username of users and employees
# If the username of a user matches the username of an employee, return the employee details
            

def emp_details(request):
    for u in users:
        for e in emps:
            if u.username == e.username:
                return render(request,"emp/employee.html")
