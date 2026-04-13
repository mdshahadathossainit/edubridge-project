from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import RegistrationForm, UserUpdateForm
from courses.models import Course, Enrollment, Homework
from members.models import Teacher, Student

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return redirect('dashboard')

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def dashboard(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if profile.user_type == 'teacher':
        return redirect('teacher_dashboard')
    elif profile.user_type == 'admin':
        return redirect('admin_dashboard')
    return redirect('student_dashboard')

@login_required
def teacher_dashboard(request):
    teacher = Teacher.objects.filter(user=request.user).first()
    courses = Course.objects.filter(instructor=teacher) if teacher else []
    
    course_data = []
    for course in courses:
        student_count = Enrollment.objects.filter(course=course).count()
        course_data.append({'course': course, 'students': student_count})
        
    return render(request, 'users/teacher_dashboard.html', {
        'course_data': course_data,
        'total_courses': len(courses)
    })

@login_required
def student_dashboard(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    enrolled_courses = [e.course for e in enrollments]
    homeworks = Homework.objects.filter(course__in=enrolled_courses).order_by('-due_date')
    
    return render(request, 'users/student_dashboard.html', {
        'enrollments': enrollments,
        'homeworks': homeworks
    })

@login_required
def admin_dashboard(request):
    profiles = Profile.objects.all()
    return render(request, 'users/admin_dashboard.html', {'profiles': profiles})

@login_required
def profile_view(request):
    return render(request, 'users/profile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated.')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password changed.')
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {'form': form})
