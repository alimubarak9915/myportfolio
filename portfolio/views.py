from django.shortcuts import render
from django.views import View


class Portfolio(View):

    def get(self, request):
        context = {
            'title': 'Mubarak Portfolio',
            'nb': 'portfolio',
        }
        return render(self.request, 'portfolio/portfolio.html', context)


portfolio_view = Portfolio.as_view()


class Services(View):
    def get(self, request):
        context = {
            'title': 'Mubarak Services',
            'nb': 'services',
        }
        return render(self.request, 'portfolio/services.html', context)


services_view = Services.as_view()


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
