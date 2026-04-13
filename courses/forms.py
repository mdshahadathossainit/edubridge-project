from django import forms
from .models import Course, Homework

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'instructor', 'duration', 'price', 'image']

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['course', 'description', 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
