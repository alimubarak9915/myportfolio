from django.urls import path
from .views import (
    portfolio_view,
    projects_view,
    contact_view,
    resume_download_view,
    send_email_view
)

app_name = 'portfolio'

urlpatterns = [
    path('', portfolio_view, name='portfolio-page'),
    path('projects/', projects_view, name='projects-page'),
    path('contact/', contact_view, name='contact-page'),
    path('resume/', resume_download_view, name='resume'),
    path('send-email/', send_email_view, name='send-email'),
]
