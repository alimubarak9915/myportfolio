from django.contrib import messages
from django.shortcuts import render
from django.views import View
from django.http import FileResponse
import os


class Portfolio(View):

    def get(self, request):
        context = {
            'title': 'Mubarak Portfolio',
            'nb': 'portfolio',
        }
        return render(self.reuest, 'portfolio/portfolio.html', context)


portfolio_view = Portfolio.as_view()


class Projects(View):
    def get(self, request):
        context = {
            'title': 'Mubarak Projects',
            'nb': 'projects',
        }
        return render(self.request, 'portfolio/projects.html', context)


projects_view = Projects.as_view()


class Contact(View):
    def get(self, request):
        context = {
            'title': 'Mubarak Contact',
            'nb': 'contact',
        }
        return render(self.request, 'portfolio/contact.html', context)


contact_view = Contact.as_view()


class ResumeDownload(View):
    RESUME_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'media', 'resume',
                               'Mubarak_Ali.pdf')

    def get(self, request):
        return FileResponse(open(self.RESUME_PATH, 'rb'), content_type='application/pdf')


resume_download_view = ResumeDownload.as_view()


class SendEmail(View):
    def post(self, request):
        data = self.request.POST
        if check := self.send_app_email(data):
            messages.success(self.request, 'Email sent successfully')
        else:
            messages.error(self.request, 'Email not sent')
        return render(self.request, 'portfolio/contact.html', {'title': 'Mubarak Contact', 'nb': 'contact'})

    @staticmethod
    def send_app_email(data):
        from django.core.mail import send_mail
        from django.conf import settings
        try:
            subject = f'New message from portfolio website from {data.get("name")}'
            message = f'Name: {data.get("name")}\nEmail: {data.get("email")}\nMessage: {data.get("message")}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['alimubarak9915@gmail.com']
            check = send_mail(subject, message, email_from, recipient_list)
            return check == 1
        except Exception as e:
            import traceback
            print(traceback.format_exc())
            print(e)


send_email_view = SendEmail.as_view()
