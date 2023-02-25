from django.urls import path
from .views import (
    portfolio_view,
    services_view,
    projects_view,
    contact_view,
)

app_name = 'portfolio'

urlpatterns = [
    path('', portfolio_view, name='portfolio-page'),
    path('services/', services_view, name='services-page'),
    path('projects/', projects_view, name='projects-page'),
    path('contact/', contact_view, name='contact-page'),
]
