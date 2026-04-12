from django.contrib import admin
from django import forms
from django.contrib.auth.models import User
from .models import SiteSettings, Teacher, Student, SuccessStory, SlideshowImage
from users.models import Profile

class TeacherAdminForm(forms.ModelForm):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

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

        if not change:
            if User.objects.filter(username=username).exists():
                raise ValueError(f"Username '{username}' already exists.")

            user = User.objects.create_user(
                username=username,
                email=obj.email,
                password=password
            )
            obj.user = user
            profile, created = Profile.objects.get_or_create(user=user)
            profile.user_type = 'teacher'
            profile.save()
        else:
            if password and obj.user:
                obj.user.set_password(password)
                obj.user.save()

        super().save_model(request, obj, form, change)

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if SiteSettings.objects.exists():
            return False
        return True
    list_display = ('site_name',)
    fields = ('site_name', 'logo', 'background_image')

@admin.register(SuccessStory)
class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ('student_name',)

@admin.register(SlideshowImage)
class SlideshowImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'image')

admin.site.register(Student)
