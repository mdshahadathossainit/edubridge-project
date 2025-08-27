from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),  # এটা যোগ করো
    path('<int:course_id>/enroll/', views.enroll_in_course, name='enroll_in_course'),
    path('my-courses/', views.my_courses, name='my_courses'),
    path('create/', views.create_course, name='create_course'),
]
