from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('matrix:index')
    else:
        form = UserLoginForm()
    context = {
        'login_form': form,
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = UserRegistrationForm()
    context = {
        'registration_form': form,
    }
    return render(request, 'users/registration.html', context)    