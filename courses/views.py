from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Enrollment
from .models import Enrollment
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .forms import CourseForm

@login_required
def enroll_in_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    enrollment, created = Enrollment.objects.get_or_create(student=request.user, course=course)

    if created:
        messages.success(request, f"You have been enrolled in {course.title}.")
    else:
        messages.info(request, f"You are already enrolled in {course.title}.")

    return redirect('course_list')  #  course list view name

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})




@login_required
def my_courses(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request, 'courses/my_courses.html', {'enrollments': enrollments})




@staff_member_required
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'courses/create_course.html', {'form': form})





@login_required
def my_courses(request):
    enrolled_courses = Enrollment.objects.filter(student=request.user)
    return render(request, 'courses/my_courses.html', {'enrolled_courses': enrolled_courses})



@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})

def home_page(request):
    success_stories = SuccessStory.objects.all()
    slideshow_images = SlideshowImage.objects.all()

    context = {
        'success_stories': success_stories,
        'slideshow_images': slideshow_images,
    }

    return render(request, 'home.html', context)