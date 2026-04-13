from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Enrollment, Homework
from .forms import CourseForm, HomeworkForm
from members.models import Teacher

@login_required
def add_homework(request):
    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        messages.error(request, "Only instructors can add homework.")
        return redirect('dashboard')

    if request.method == 'POST':
        form = HomeworkForm(request.POST)
        if form.is_valid():
            homework = form.save(commit=False)
            if homework.course.instructor == teacher:
                homework.save()
                messages.success(request, "Homework added successfully.")
                return redirect('teacher_dashboard')
            else:
                messages.error(request, "Unauthorized course selection.")
    else:
        form = HomeworkForm()
        form.fields['course'].queryset = Course.objects.filter(instructor=teacher)
    
    return render(request, 'courses/add_homework.html', {'form': form})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})

@login_required
def enroll_in_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.user.profile.user_type != 'student':
        messages.error(request, "Only students can enroll in courses.")
        return redirect('course_detail', course_id=course.id)
        
    Enrollment.objects.get_or_create(student=request.user, course=course)
    messages.success(request, f"Successfully enrolled in {course.title}")
    return redirect('student_dashboard')

@login_required
def my_courses(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request, 'courses/my_courses.html', {'enrollments': enrollments})

@login_required
def create_course(request):
    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        messages.error(request, "You must be a registered teacher to create courses.")
        return redirect('course_list')

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = teacher
            course.save()
            messages.success(request, "Course created successfully.")
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'courses/create_course.html', {'form': form})
