from django.contrib import admin
from .models import WeeklyService, HomePageSection, SpecialEvent, Culte, Video

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

@admin.register(SpecialEvent)
class SpecialEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'theme', 'location', 'time', 'expire_after_days', 'est_culte_de_la_semaine')
    list_filter = ('date', 'theme', 'est_culte_de_la_semaine')

@admin.register(Culte)
class CulteAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_song')
    search_fields = ('title', 'description_main', 'description_secondary')
    list_filter = ('date', 'is_song')
    filter_horizontal = ('videos',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'is_song')
    search_fields = ('title',)
