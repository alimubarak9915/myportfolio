from django.contrib import admin
from .models import VisitorDetails


@admin.register(VisitorDetails)
class VisitorDetailsAdmin(admin.ModelAdmin):
    list_display = ['ip', 'last_visited', 'visited_count']
