from django.contrib import admin
from .models import WeeklyService, HomePageSection

@admin.register(WeeklyService)
class WeeklyServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    search_fields = ('title', 'description')
    list_filter = ('date', 'location')

@admin.register(HomePageSection)
class HomePageSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'section_type', 'display_order', 'is_active')
    list_filter = ('section_type', 'is_active')
    list_editable = ('display_order', 'is_active')