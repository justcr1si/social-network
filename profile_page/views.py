from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static

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


def profile(request, user_id=None):
    if user_id:
        user = User.objects.get(pk=user_id)
        return render(request, 'profile_page/profile.html', {'user': user})
    return render(request, 'profile_page/profile.html')


@login_required(login_url='/profile/login/')
def process_profile_photo(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        image = request.FILES.get('file')
        if image:
            user.image = image
        else:
            user.image = static("assets/img/unknown-user.jpg")
        user.save()

    return redirect('profile:profile')


@login_required(login_url='/profile/login/')
def process_profile_description(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        description = request.POST.get('description')
        if description:
            user.description = description
            user.save()

    return redirect('profile:profile')


@login_required(login_url='/profile/login/')
def delete_user_image(request, user_id):
    user = User.objects.get(pk=user_id)
    if user.image:
        user.image.delete()
        user.save()
    return redirect('profile:profile')
