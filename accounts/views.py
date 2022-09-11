from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials!')
            return redirect('login')
    else:
        return render(request, 'login.html')
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken!')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken!')
                return redirect('signup')
            elif username == '' or email == '' or first_name == '' or password1 == '':
                messages.info(request, 'Please fill all the fields!')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=password1)
                user.save()
                print("user created")
                return redirect('/')
        else:
            messages.info(request, 'password not matched!')
            return redirect('signup')
    else:
        return render(request, 'signup.html')
def logout(request):
    auth.logout(request)
    return redirect('/')