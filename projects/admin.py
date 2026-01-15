from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'status', 'order', 'created_at']
    list_filter = ['featured', 'status', 'created_at']
    search_fields = ['title', 'description', 'tech_stack']
    list_editable = ['featured', 'order', 'status']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-featured', 'order', '-created_at']

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'tech_stack')
        }),
        ('URLs', {
            'fields': ('github_url', 'live_url', 'thumbnail_url')
        }),
        ('Management', {
            'fields': ('featured', 'order', 'status')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ['created_at', 'updated_at']
