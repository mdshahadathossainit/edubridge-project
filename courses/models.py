from django.db import models
from django.utils import timezone
from django.conf import settings


# নতুন Teacher মডেল
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # instructor এখন ForeignKey
    instructor = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    duration = models.PositiveIntegerField(help_text="Duration in weeks")
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    def __str__(self):
        return self.title


class Enrollment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')  # prevent duplicate enrollments

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.title}"
