from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Project(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('archived', 'Archived'),
    ]

    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200, help_text="Comma-separated e.g. React, Tailwind, Django")
    highlights = models.TextField(blank=True, help_text="Comma-separated highlights e.g. Feature 1, Feature 2")
    github_url = models.URLField(blank=True)
    github_backend_url = models.URLField(blank=True, help_text="Backend repo URL if separate")
    live_url = models.URLField(blank=True)
    thumbnail_url = models.URLField(blank=True)

    # New fields for enhanced management
    featured = models.BooleanField(default=False, help_text="Highlight this project")
    order = models.IntegerField(default=0, help_text="Display order (lower numbers first)")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-featured', 'order', '-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:140]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Blog(models.Model):
    """Blog post model for managing blog content"""
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    content = models.TextField(help_text="HTML content from rich text editor")
    excerpt = models.TextField(max_length=300, blank=True, help_text="Short description for preview")
    thumbnail_url = models.URLField(blank=True)

    # Management fields
    featured = models.BooleanField(default=False, help_text="Feature this blog post")
    published = models.BooleanField(default=False, help_text="Publish this post")
    order = models.IntegerField(default=0, help_text="Display order (lower numbers first)")

    # Timestamps
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-featured', 'order', '-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:220]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
