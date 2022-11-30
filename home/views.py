from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Video
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, "base.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if len(username) < 5:
            messages.error(
                request, " username mustbe greater than 10 characters")
            return render(request, 'signup.html')
        if not username.isalnum():
            messages.error(request, " username mustbe be alphanumeric")
            return render(request, 'signup.html')
        if pass1 != pass2:
            messages.error(request, " passwords not matching")
            return render(request, 'signup.html')

        elif len(username) >= 5 and username.isalnum() and pass1 == pass2:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = name
            myuser.save()
            messages.success(request, ' : user successfully created')
            return redirect('/login')
    return render(request, 'signup.html')


def handlelogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass3 = request.POST['password']
        # print(username,pass3)
        user = authenticate(username=username, password=pass3)
        if user is not None:
            login(request, user)
            messages.success(request, username+" successfully loged in ")
            return redirect("/")
        else:
            messages.error(request, "invalid credentials")
            return render(request, 'login.html')
    return render(request, 'login.html')


def handlelogout(request):
    logout(request)
    messages.success(request, " successfully logged out ")
    return redirect('/')
