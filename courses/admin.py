from django.contrib import admin
from .models import Course, Enrollment, Homework

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor')
    list_select_related = ('instructor',)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrolled_at')
    list_filter = ('course', 'enrolled_at')

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('course', 'due_date', 'created_at')
