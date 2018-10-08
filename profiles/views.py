from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Users
# Create your views here.
def login(request):
    pass

def register(request):
    if (request.method == 'POST'):
        form = UserForm(request.POST)
        print (form.is_valid())
        print (form)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = Users(username=username, email=email, password=password)
            user.save()
            # newuser = Users()
            # newuser.username = form.cleaned_data['username']
            # newuser.email = form.cleaned_data['email']
            # newuser.password = form.cleaned_data['password']
            # newuser.save()
        return redirect('index')