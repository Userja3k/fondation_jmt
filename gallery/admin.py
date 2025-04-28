from django.contrib import admin
from .models import GalleryItem, GalleryCollection, GalleryCollectionItem

class GalleryCollectionItemInline(admin.TabularInline):
    model = GalleryCollectionItem
    extra = 3

@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'description')
    list_filter = ('date',)

@admin.register(GalleryCollection)
class GalleryCollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'description')
    list_filter = ('date',)
    inlines = [GalleryCollectionItemInline]