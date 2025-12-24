from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Enrollment, Course, Chapter, Page

# Home page
def home(request):
    return render(request, "pages/home.html")

# My Courses (ONLY enrolled courses)
@login_required
def my_courses(request):
    courses = Course.objects.filter(
        enrollment__user=request.user
    ).distinct()
    return render(request, 'pages/my_courses.html', {'courses': courses})

# Course detail (protected)
@login_required
def course_detail(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    if not Enrollment.objects.filter(user=request.user, course=course).exists():
        return render(request, 'pages/not_enrolled.html', {'course': course})
    chapters = course.chapters.all()
    return render(request, 'pages/course_detail.html', {
        'course': course,
        'chapters': chapters
    })

# Chapter detail (protected)
@login_required
def chapter_detail(request, course_slug, chapter_slug):
    course = get_object_or_404(Course, slug=course_slug)
    if not Enrollment.objects.filter(user=request.user, course=course).exists():
        return redirect('my_courses')
    chapter = get_object_or_404(Chapter, course=course, slug=chapter_slug)
    pages = chapter.pages.all()
    return render(request, 'pages/chapter_detail.html', {
        'course': course,
        'chapter': chapter,
        'pages': pages
    })

# Page detail (protected)
@login_required
def page_detail(request, course_slug, chapter_slug, page_slug):
    course = get_object_or_404(Course, slug=course_slug)
    if not Enrollment.objects.filter(user=request.user, course=course).exists():
        return redirect('my_courses')
    chapter = get_object_or_404(Chapter, course=course, slug=chapter_slug)
    page = get_object_or_404(Page, chapter=chapter, slug=page_slug)
    return render(request, 'pages/page_detail.html', {
        'course': course,
        'chapter': chapter,
        'page': page
    })
