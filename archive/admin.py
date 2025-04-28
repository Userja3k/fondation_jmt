from django.contrib import admin
from .models import ArchivedService, Debate

@admin.register(ArchivedService)
class ArchivedServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'theme')
    search_fields = ('title', 'theme', 'description')
    list_filter = ('date',)

@admin.register(Debate)
class DebateAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'date')
    search_fields = ('title', 'topic', 'description')
    list_filter = ('date',)