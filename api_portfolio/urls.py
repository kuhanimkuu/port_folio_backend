"""
URL configuration for api_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from projects.views import (
    # Public project views
    ProjectListView, ProjectDetailView,
    # Admin project views
    ProjectAdminListView, ProjectUpdateView, ProjectDeleteView, project_reorder,
    # Public blog views
    BlogListView, BlogDetailView,
    # Admin blog views
    BlogAdminListView, BlogCreateView, BlogUpdateView, BlogDeleteView, blog_reorder,
    # Image upload
    image_upload
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # Authentication endpoints
    path("api/auth/", include("authentication.urls")),

    # Public project endpoints
    path("api/projects/", ProjectListView.as_view(), name="project-list"),
    path("api/projects/<slug:slug>/", ProjectDetailView.as_view(), name="project-detail"),

    # Public blog endpoints
    path("api/blogs/", BlogListView.as_view(), name="blog-list"),
    path("api/blogs/<slug:slug>/", BlogDetailView.as_view(), name="blog-detail"),

    # Admin project endpoints
    path("api/admin/projects/", ProjectAdminListView.as_view(), name="admin-project-list"),
    path("api/admin/projects/<int:pk>/", ProjectUpdateView.as_view(), name="admin-project-update"),
    path("api/admin/projects/<int:pk>/delete/", ProjectDeleteView.as_view(), name="admin-project-delete"),
    path("api/admin/projects/reorder/", project_reorder, name="admin-project-reorder"),

    # Admin blog endpoints
    path("api/admin/blogs/", BlogAdminListView.as_view(), name="admin-blog-list"),
    path("api/admin/blogs/create/", BlogCreateView.as_view(), name="admin-blog-create"),
    path("api/admin/blogs/<int:pk>/", BlogUpdateView.as_view(), name="admin-blog-update"),
    path("api/admin/blogs/<int:pk>/delete/", BlogDeleteView.as_view(), name="admin-blog-delete"),
    path("api/admin/blogs/reorder/", blog_reorder, name="admin-blog-reorder"),

    # Image upload endpoint
    path("api/admin/upload/", image_upload, name="admin-image-upload"),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
