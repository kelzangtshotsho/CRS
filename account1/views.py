from django.shortcuts import render

# Create your views here.
from django.core.checks import messages
from django.contrib import messages
# from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

# Create your views here.

def login1(request):

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('rent')
        else:
            messages.info(request,'**invalid credentials**')
            return redirect(login1)
    else:
        return render(request, 'login1.html')



def register1(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        # CID = request.POST['CID']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'**Username already taken**')
                return redirect('register1')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'**Email already taken**')
                return redirect('register1')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('User created')
                return redirect('login1')
        else:
            messages.info(request,'**Password does not match**')
            return redirect('register1')
            return redirect('/')

    else:       
        return render(request, 'register1.html')





def logout(request):
    auth.logout(request)
    return redirect('/')