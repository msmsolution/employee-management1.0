from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None and user.username == "admin":
            login(request, user)
            # Redirect to a success page.
            return redirect("/emp/home/")
        elif user is not None and user.username != "admin":
            login(request, user)
            return redirect("emp/employee")
        else:
            # Return an 'invalid login' error message.
            messages.error(request, 'Invalid username or password. Check with your manager')

    return render(request,"authenticate/login.html",{})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect("/accounts/login/")
