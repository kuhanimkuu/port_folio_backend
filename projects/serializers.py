from rest_framework import serializers
from .models import Project, Blog
import bleach

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'description', 'tech_stack',
            'github_url', 'live_url', 'thumbnail_url',
            'featured', 'order', 'status',
            'created_at', 'updated_at'
        ]


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
