from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    USER_TYPES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('admin', 'Admin'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)

    def __str__(self):
        return f"{self.user.username} - {self.user_type}"


class SuccessStory(models.Model):
    """সাফল্যের গল্প সংরক্ষণের জন্য মডেল"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='success_stories/')

    def __str__(self):
        return self.title


class SlideshowImage(models.Model):
    """হোমপেজের স্লাইডারের জন্য ছবি"""
    image = models.ImageField(upload_to='slideshows/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption or "Slideshow Image"