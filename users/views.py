from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
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
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Успешно')
            return redirect('users:login')
    else:
        form = UserRegistrationForm()
    context = {
        'registration_form': form,
    }
    return render(request, 'users/registration.html', context)    


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            redirect('users:profile')
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'profile_form': form,
    }
    return render(request, 'users/profile.html', context)