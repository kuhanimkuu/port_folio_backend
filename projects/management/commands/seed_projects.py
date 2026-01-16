from django.core.management.base import BaseCommand
from projects.models import Project


class Command(BaseCommand):
    help = 'Seed the database with portfolio projects'

    def handle(self, *args, **options):
        projects_data = [
            {
                "title": "Globetrotter - Travel Agency Platform",
                "description": "A comprehensive travel agency platform allowing users to explore tourism destinations and book hotels, cars, flights and tour packages. Features Stripe and Amadeus API integrations for payments and travel data. Tour organizers can create and manage their own packages. Includes automatic availability tracking to prevent double bookings and a fully responsive interface.",
                "tech_stack": "React, Django, PostgreSQL, Cloudinary, Stripe API, Amadeus API",
                "highlights": "Built adapters for Stripe and Amadeus APIs, Role-based features for users and tour organizers, Automatic availability tracking to prevent double bookings, Fully responsive interface for desktop and mobile",
                "github_url": "https://github.com/kuhanimkuu/GlobeTrotter_frontend",
                "github_backend_url": "https://github.com/kuhanimkuu/GlobeTrotter_backend",
                "live_url": "https://globe-trotter-frontend-git-main-david-murungas-projects.vercel.app",
                "featured": True,
                "order": 1,
            },
            {
                "title": "Event Booking Platform",
                "description": "A full-stack event management platform with user authentication, event creation, booking system, and automatic PDF ticket generation. Users can browse events, book tickets, and receive downloadable PDF tickets via email.",
                "tech_stack": "Django, PostgreSQL, Cloudinary, PDF Generation",
                "highlights": "User authentication and role-based access, PDF ticket generation and email delivery, Event management dashboard, Cloudinary integration for image uploads",
                "github_url": "https://github.com/kuhanimkuu/event_booking_platform",
                "github_backend_url": "",
                "live_url": "https://eventbookingplatform-production.up.railway.app/",
                "featured": True,
                "order": 2,
            },
            {
                "title": "Portfolio Website",
                "description": "A responsive portfolio website showcasing projects and skills with a modern glassmorphism design. Features multi-page navigation, animated geometric backgrounds, light/dark theme support, and a contact form.",
                "tech_stack": "React, Tailwind CSS, Framer Motion, Django REST Framework",
                "highlights": "Glassmorphism design with animated backgrounds, Multi-page React application with smooth transitions, Admin panel for content management, Responsive design for all screen sizes",
                "github_url": "https://github.com/kuhanimkuu/port_folio",
                "github_backend_url": "",
                "live_url": "https://port-folio-ten-blue.vercel.app/",
                "featured": False,
                "order": 3,
            },
            {
                "title": "Video Streaming Platform",
                "description": "A React-based video streaming platform where users can watch and browse videos, similar to YouTube. Features video categories, search functionality, and a clean responsive UI.",
                "tech_stack": "React, Tailwind CSS, HTML, CSS",
                "highlights": "Video browsing and streaming functionality, Search and category filtering, Responsive design, Clean and modern UI",
                "github_url": "https://github.com/kuhanimkuu/youtube-clone",
                "github_backend_url": "",
                "live_url": "https://youtube-clone-kappa-red.vercel.app/",
                "featured": False,
                "order": 4,
            },
            {
                "title": "Weather App",
                "description": "A responsive weather application that shows real-time weather information for any location. Features current conditions, forecasts, and location search with a clean, intuitive interface.",
                "tech_stack": "HTML, CSS, JavaScript, Weather API",
                "highlights": "Real-time weather data fetching, Location search functionality, Responsive design, Clean weather display UI",
                "github_url": "https://github.com/kuhanimkuu/weather-app",
                "github_backend_url": "",
                "live_url": "https://weather-app-2-np7i.vercel.app/",
                "featured": False,
                "order": 5,
            },
        ]

        for project_data in projects_data:
            project, created = Project.objects.update_or_create(
                title=project_data["title"],
                defaults=project_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created: {project.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Updated: {project.title}'))

        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully seeded {len(projects_data)} projects!'))
