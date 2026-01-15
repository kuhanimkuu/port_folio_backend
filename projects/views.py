from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    UpdateAPIView, DestroyAPIView
)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
from .models import Project, Blog
from .serializers import ProjectSerializer, BlogSerializer, BlogAdminSerializer


# ============ PROJECT VIEWS ============

class ProjectListView(ListAPIView):
    """Public list of projects"""
    queryset = Project.objects.filter(status='active').order_by('-featured', 'order', '-created_at')
    serializer_class = ProjectSerializer


class ProjectDetailView(RetrieveAPIView):
    """Public project detail"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "slug"


class ProjectAdminListView(ListAPIView):
    """Admin: List all projects"""
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all().order_by('-featured', 'order', '-created_at')
    serializer_class = ProjectSerializer


class ProjectUpdateView(UpdateAPIView):
    """Admin: Update project"""
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDeleteView(DestroyAPIView):
    """Admin: Delete project"""
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def project_reorder(request):
    """Admin: Reorder projects"""
    projects_data = request.data.get('projects', [])

    for project_data in projects_data:
        project_id = project_data.get('id')
        new_order = project_data.get('order')

        if project_id is not None and new_order is not None:
            Project.objects.filter(id=project_id).update(order=new_order)

    return Response({'detail': 'Projects reordered successfully'}, status=status.HTTP_200_OK)


# ============ BLOG VIEWS ============

class BlogListView(ListAPIView):
    """Public: List published blogs"""
    queryset = Blog.objects.filter(published=True).order_by('-featured', 'order', '-created_at')
    serializer_class = BlogSerializer


class BlogDetailView(RetrieveAPIView):
    """Public: Blog detail by slug"""
    queryset = Blog.objects.filter(published=True)
    serializer_class = BlogSerializer
    lookup_field = "slug"


class BlogAdminListView(ListAPIView):
    """Admin: List all blogs (including unpublished)"""
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all().order_by('-featured', 'order', '-created_at')
    serializer_class = BlogAdminSerializer


class BlogCreateView(CreateAPIView):
    """Admin: Create new blog"""
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all()
    serializer_class = BlogAdminSerializer


class BlogUpdateView(UpdateAPIView):
    """Admin: Update blog"""
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all()
    serializer_class = BlogAdminSerializer


class BlogDeleteView(DestroyAPIView):
    """Admin: Delete blog"""
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all()
    serializer_class = BlogAdminSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def blog_reorder(request):
    """Admin: Reorder blogs"""
    blogs_data = request.data.get('blogs', [])

    for blog_data in blogs_data:
        blog_id = blog_data.get('id')
        new_order = blog_data.get('order')

        if blog_id is not None and new_order is not None:
            Blog.objects.filter(id=blog_id).update(order=new_order)

    return Response({'detail': 'Blogs reordered successfully'}, status=status.HTTP_200_OK)


# ============ IMAGE UPLOAD ============

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def image_upload(request):
    """Admin: Upload image and return URL"""
    if 'image' not in request.FILES:
        return Response({'error': 'No image file provided'}, status=status.HTTP_400_BAD_REQUEST)

    image_file = request.FILES['image']

    # Validate file type
    allowed_types = ['image/jpeg', 'image/png', 'image/webp', 'image/jpg']
    if image_file.content_type not in allowed_types:
        return Response(
            {'error': 'Invalid file type. Only JPG, PNG, and WEBP are allowed.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Validate file size (5MB max)
    if image_file.size > 5242880:
        return Response(
            {'error': 'File too large. Maximum size is 5MB.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Save file
    file_name = default_storage.save(
        f'uploads/{image_file.name}',
        ContentFile(image_file.read())
    )

    # Return full URL
    file_url = request.build_absolute_uri(default_storage.url(file_name))

    return Response({'url': file_url}, status=status.HTTP_201_CREATED)
