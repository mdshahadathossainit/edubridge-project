# members/views.py

from django.shortcuts import render, get_object_or_404
from .models import Course, Teacher, SiteSettings, SuccessStory, SlideshowImage


def home_page(request):
    """
    Handles the homepage view, retrieving all necessary data for display.
    This includes popular courses, teachers, site settings, success stories, and slideshow images.
    """
    # Fetching courses (top 6)
    courses = Course.objects.all()[:6]
    # Fetching teachers (top 4)
    teachers = Teacher.objects.all()[:4]
    # Fetching site settings
    site_settings = SiteSettings.objects.first()
    # Fetching all success stories
    success_stories = SuccessStory.objects.all()
    # Fetching all slideshow images
    slideshow_images = SlideshowImage.objects.all()

    # Creating the context dictionary to pass data to the template
    context = {
        'courses': courses,
        'teachers': teachers,
        'site_settings': site_settings,
        'success_stories': success_stories,
        'slideshow_images': slideshow_images,
    }

    # Rendering the homepage template with the prepared context
    return render(request, 'members/home.html', context)


def teachers_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'members/teachers_list.html', {'teachers': teachers})


def teacher_profile(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    return render(request, 'members/teacher_profile.html', {'teacher': teacher})
