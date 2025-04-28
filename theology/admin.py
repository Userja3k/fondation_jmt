from django.contrib import admin
from .models import TheologyCourse

@admin.register(TheologyCourse)
class TheologyCourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'course_type', 'location')
    search_fields = ('title', 'description')
    list_filter = ('date', 'course_type')