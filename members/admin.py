# members/admin.py

from django.contrib import admin
from django import forms
from django.contrib.auth.models import User
from .models import SiteSettings, Teacher, Course, SuccessStory, SlideshowImage

# কাস্টম ফর্ম যাতে username এবং password ইনপুট নেওয়া যায়
class TeacherAdminForm(forms.ModelForm):
    username = forms.CharField(required=True, help_text="Set a username for the teacher's user account.")
    password = forms.CharField(widget=forms.PasswordInput, required=True, help_text="Set a password for the teacher's user account.")

    class Meta:
        model = Teacher
        fields = ('name', 'email', 'subject', 'bio', 'photo', 'username', 'password')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    form = TeacherAdminForm
    list_display = ('name', 'email', 'subject')

    def save_model(self, request, obj, form, change):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        if not change:  # নতুন Teacher তৈরি হলে
            # Username ডুপ্লিকেট চেক
            if User.objects.filter(username=username).exists():
                raise ValueError(f"Username '{username}' already exists. Please choose another.")

            # নতুন User তৈরি
            user = User.objects.create_user(
                username=username,
                email=obj.email,
                password=password
            )
            obj.user = user
        else:
            # পাসওয়ার্ড আপডেট হলে পরিবর্তন করা হবে
            if password and obj.user:
                obj.user.set_password(password)
                obj.user.save()

        super().save_model(request, obj, form, change)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # একটির বেশি SiteSettings না বানানোর জন্য সীমাবদ্ধতা
        if SiteSettings.objects.exists():
            return False
        return True
    list_display = ('site_name',)
    fields = ('site_name', 'logo', 'background_image')

# Course মডেলটি রেজিস্টার করা হচ্ছে
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor')
    list_select_related = ('instructor',)

# SuccessStory মডেলটি রেজিস্টার করা হচ্ছে
@admin.register(SuccessStory)
class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ('student_name',)

# SlideshowImage মডেলটি রেজিস্টার করা হচ্ছে
@admin.register(SlideshowImage)
class SlideshowImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'image')
