from django.contrib import admin

from .models import URLS

@admin.register(URLS)
class URLAdmin(admin.ModelAdmin):
    list_display = ('visited', 'text', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('url',)