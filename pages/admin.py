from django.contrib import admin
from django.contrib.auth.models import User
from .models import Enrollment

class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 0  # do not show extra blank rows

# Unregister default User admin first
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.models import User
admin.site.unregister(User)

# Re-register User admin with Enrollment inline
@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    inlines = [EnrollmentInline]

from django.contrib import admin
from .models import Course, Chapter, Page, Enrollment

# Courses
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_active', 'created_at')
    prepopulated_fields = {'slug': ('title',)}

# Chapters
@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('course',)

# Pages
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'chapter', 'order')
    list_filter = ('chapter',)

# Enrollments
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enrolled_at')
    list_filter = ('course', 'user')
