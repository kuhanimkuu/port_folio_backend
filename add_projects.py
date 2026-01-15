import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_portfolio.settings')
django.setup()

from projects.models import Project

# Clear existing projects
Project.objects.all().delete()

# Add projects
projects = [
    {
        'title': 'Event Booking Platform',
        'description': 'Full-stack booking app: ticketing, authentication, and PDF receipts. Frontend demo uses React + Tailwind.',
        'tech_stack': 'React, Tailwind, Django, PostgreSQL',
        'github_url': 'https://github.com/kuhanimkuu/event_booking_platform',
        'live_url': 'https://event-booking-platform-zcql.onrender.com/',
        'thumbnail_url': 'src/assets/event.png',
        'featured': True,
        'order': 1,
        'status': 'active'
    },
    {
        'title': 'Video Streaming Platform',
        'description': 'A React-based video streaming platform where users can watch and browse videos, similar to YouTube.',
        'tech_stack': 'React, Tailwind, HTML, CSS',
        'github_url': 'https://github.com/kuhanimkuu/youtube-clone',
        'live_url': 'https://youtube-clone-kappa-red.vercel.app/',
        'thumbnail_url': 'src/assets/video.png',
        'featured': False,
        'order': 2,
        'status': 'active'
    },
    {
        'title': 'Weather App',
        'description': 'A responsive weather app built with HTML, CSS, and JavaScript that shows real-time weather information for any location.',
        'tech_stack': 'HTML, CSS, JavaScript',
        'github_url': 'https://github.com/kuhanimkuu/weather-app',
        'live_url': 'https://weather-app-2-np7i.vercel.app/',
        'thumbnail_url': 'src/assets/weather.png',
        'featured': True,
        'order': 3,
        'status': 'active'
    }
]

for proj_data in projects:
    Project.objects.create(**proj_data)

print(f"Added {len(projects)} projects to database")
print("\nProjects:")
for p in Project.objects.all():
    print(f"  - {p.title} (featured: {p.featured}, order: {p.order})")
