from rest_framework import serializers
from .models import Project, Blog
import bleach

class ProjectSerializer(serializers.ModelSerializer):
    tech = serializers.SerializerMethodField()
    highlights = serializers.SerializerMethodField()
    github = serializers.URLField(source='github_url', read_only=True)
    github_backend = serializers.URLField(source='github_backend_url', read_only=True)
    live = serializers.URLField(source='live_url', read_only=True)
    image = serializers.URLField(source='thumbnail_url', read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'description', 'tech', 'highlights',
            'github', 'github_backend', 'live', 'image',
            'featured', 'order', 'status',
            'created_at', 'updated_at'
        ]

    def get_tech(self, obj):
        """Convert comma-separated tech_stack to array"""
        if obj.tech_stack:
            return [t.strip() for t in obj.tech_stack.split(',') if t.strip()]
        return []

    def get_highlights(self, obj):
        """Convert comma-separated highlights to array"""
        if obj.highlights:
            return [h.strip() for h in obj.highlights.split(',') if h.strip()]
        return []


class BlogSerializer(serializers.ModelSerializer):
    """Serializer for public blog posts (published only)"""

    class Meta:
        model = Blog
        fields = [
            'id', 'title', 'slug', 'content', 'excerpt', 'thumbnail_url',
            'featured', 'created_at', 'updated_at'
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at']

    def validate_content(self, value):
        """Sanitize HTML content to prevent XSS attacks"""
        allowed_tags = ['p', 'h2', 'h3', 'h4', 'strong', 'em', 'u', 'ul', 'ol', 'li',
                       'a', 'img', 'code', 'pre', 'blockquote', 'br']
        allowed_attributes = {
            'a': ['href', 'title'],
            'img': ['src', 'alt']
        }
        return bleach.clean(value, tags=allowed_tags, attributes=allowed_attributes)


class BlogAdminSerializer(serializers.ModelSerializer):
    """Serializer for admin blog management (includes unpublished)"""

    class Meta:
        model = Blog
        fields = [
            'id', 'title', 'slug', 'content', 'excerpt', 'thumbnail_url',
            'featured', 'published', 'order', 'created_at', 'updated_at'
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at']

    def validate_content(self, value):
        """Sanitize HTML content to prevent XSS attacks"""
        allowed_tags = ['p', 'h2', 'h3', 'h4', 'strong', 'em', 'u', 'ul', 'ol', 'li',
                       'a', 'img', 'code', 'pre', 'blockquote', 'br']
        allowed_attributes = {
            'a': ['href', 'title'],
            'img': ['src', 'alt']
        }
        return bleach.clean(value, tags=allowed_tags, attributes=allowed_attributes)
