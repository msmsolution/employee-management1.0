from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Emp

# from django admin import Users, Emp




def emp_home(request):
    emps=Emp.objects.all()
    return render(request,"emp/home.html",{'emps':emps})


def add_emp(request):
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_username=request.POST.get("emp_username")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")
        e=Emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.username=emp_username
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()
        return redirect("/emp/home/")
    return render(request,"emp/add_emp.html",{})

def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home/")

def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request,"emp/update_emp.html",{
        'emp':emp
    })

def do_update_emp(request,emp_id):
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        emp_id_temp=request.POST.get("emp_id")
        emp_username=request.POST.get("emp_username")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

        e=Emp.objects.get(pk=emp_id)

        e.name=emp_name
        e.emp_id=emp_id_temp
        e.username=emp_username
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()
    return redirect("/emp/home/")

# Approve or reject employee leave
def approve_leave(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.leave_approved=True
    emp.save()
    return redirect("/emp/home/")

def reject_leave(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.leave_approved=False
    emp.save()
    return redirect("/emp/home/")
