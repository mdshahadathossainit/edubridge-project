# courses/admin.py

from django.contrib import admin
from .models import Course, Enrollment  



@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrolled_at')
    list_filter = ('course', 'enrolled_at')
    list_select_related = ('student', 'course')


