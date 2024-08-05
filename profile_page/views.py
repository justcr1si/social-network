from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm, UserRegistrationForm
from .models import User


def login_page(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
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
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('main_page')
    else:
        form = UserRegistrationForm()

    context = {
        'form': form,
    }

    return render(request, 'profile_page/register.html', context)


@login_required(login_url='/profile/login/')
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('main_page')


def profile(request):
    return render(request, 'profile_page/profile.html')


def process_profile_photo(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        image = request.POST.get('file')
        if image:
            user.image = image
            user.save()

    return render(request, 'profile_page/profile.html')


def process_profile_description(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        description = request.POST.get('description')
        if description:
            user.description = description
            user.save()

    return render(request, 'profile_page/profile.html')
