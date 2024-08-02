from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout, login

from .forms import UserLoginForm, UserRegistrationForm


def login_page(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('main_page')
    else:
        form = UserLoginForm()

    context = {
        'form': form,
    }
    return render(request, 'profile_page/login.html', context)


def register_page(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('main_page')
    else:
        form = UserRegistrationForm()

    context = {
        'form': form,
    }

    return render(request, 'profile_page/register.html', context)


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('main_page')


def profile(request):
    return render(request, 'profile.html')
