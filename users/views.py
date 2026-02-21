from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from users.forms import UserUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .decorators import admin_required
from .models import Profile
from .models import SuccessStory, SlideshowImage

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print("--- login_view: Login successful. Redirecting to dashboard...")
            messages.success(request, "Log in success")
            return redirect('dashboard') 
            messages.error(request, "User Name wrong")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "You log in")
    return redirect('login')


@login_required
def dashboard(request):
    print("--- dashboard_view: Dashboard view is being executed!")
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    print(f"--- dashboard_view: User type is: {profile.user_type}")
    if profile.user_type == 'teacher':
        return redirect('teacher_dashboard')
    elif profile.user_type == 'student':
        return redirect('student_dashboard')
    elif profile.user_type == 'admin':
        return redirect('admin_dashboard')
    else:
        return redirect('home')


@login_required
def teacher_dashboard(request):
    return render(request, 'users/teacher_dashboard.html')


@login_required
def student_dashboard(request):
    return render(request, 'users/student_dashboard.html')


@login_required
def admin_dashboard(request):
    return render(request, 'users/admin_dashboard.html')


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile_view(request):
    return render(request, 'users/profile.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('dashboard')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {'form': form})






