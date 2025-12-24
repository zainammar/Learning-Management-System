from django.urls import path
from .views import home, my_courses, course_detail, chapter_detail, page_detail

urlpatterns = [
    path('', home, name='home'),
    path('my-courses/', my_courses, name='my_courses'),
    path('courses/<slug:course_slug>/', course_detail, name='course_detail'),
    path('courses/<slug:course_slug>/<slug:chapter_slug>/', chapter_detail, name='chapter_detail'),
    path('courses/<slug:course_slug>/<slug:chapter_slug>/<slug:page_slug>/', page_detail, name='page_detail'),
]
