from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'is_upcoming')
    search_fields = ('title', 'description')
    list_filter = ('date', 'is_upcoming', 'location')
    readonly_fields = ('is_upcoming',)