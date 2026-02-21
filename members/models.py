

from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    subject = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='teachers/', blank=True, null=True)

    def __str__(self):
        return self.name




class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    course_image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    duration = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.title


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, default='EduBridge')
    logo = models.ImageField(upload_to='site/', blank=True, null=True)
    background_image = models.ImageField(upload_to='site/', blank=True, null=True)

    def __str__(self):
        return "Site Settings"




class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment_number = models.CharField(max_length=30, unique=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class SuccessStory(models.Model):
    student_name = models.CharField(max_length=100)
    story_text = models.TextField()
    photo = models.ImageField(upload_to='success_stories/', blank=True, null=True)

    def __str__(self):
        return self.student_name

class SlideshowImage(models.Model):
    image = models.ImageField(upload_to='slideshow_images/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.caption or f'Image {self.id}'
