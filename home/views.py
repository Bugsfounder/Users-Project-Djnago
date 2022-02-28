from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# password for test user :- manisha$$$***000
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request=request,template_name='index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            return redirect('/')
        else:
            # No backend authenticated the credentials
            return render(request=request,template_name='login.html')
    return render(request=request,template_name='login.html')

def logout(request):
    return render(request=request,template_name='index.html')