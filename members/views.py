# members/views.py

from django.shortcuts import render, get_object_or_404
from .models import Course, Teacher, SiteSettings, SuccessStory, SlideshowImage


def home_page(request):

    courses = Course.objects.all()[:6]
    teachers = Teacher.objects.all()[:4]
    site_settings = SiteSettings.objects.first()
    success_stories = SuccessStory.objects.all()
    slideshow_images = SlideshowImage.objects.all()

    context = {
        'courses': courses,
        'teachers': teachers,
        'site_settings': site_settings,
        'success_stories': success_stories,
        'slideshow_images': slideshow_images,
    }

    return render(request, 'members/home.html', context)


def teachers_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'members/teachers_list.html', {'teachers': teachers})


def teacher_profile(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    return render(request, 'members/teacher_profile.html', {'teacher': teacher})
