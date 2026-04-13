from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Enrollment, Homework
from .forms import CourseForm, HomeworkForm
from members.models import Teacher

@login_required
def add_homework(request):
    teacher = get_object_or_404(Teacher, user=request.user)
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
    Enrollment.objects.get_or_create(student=request.user, course=course)
    return redirect('student_dashboard')

@login_required
def my_courses(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request, 'courses/my_courses.html', {'enrollments': enrollments})

@login_required
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'courses/create_course.html', {'form': form})
