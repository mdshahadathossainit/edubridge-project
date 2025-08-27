from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_page, name='home'),
    path('teachers/', views.teachers_list, name='teachers_list'),  # এই লাইনটা অবশ্যই থাকবে
    path('teacher/<int:id>/', views.teacher_profile, name='teacher_profile'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
