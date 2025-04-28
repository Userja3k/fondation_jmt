from django.contrib import admin
from .models import AboutContent, Founder, Partner

@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Founder)
class FounderAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')