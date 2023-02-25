from django.utils import timezone

from .models import VisitorDetails


def visitor_count(request):
    ip = request.META.get('REMOTE_ADDR')
    visitor = VisitorDetails.objects.filter(ip=ip).first()
    if visitor:
        visitor.visited_count += 1
        visitor.last_visited = timezone.now()
        visitor.save()
    else:
        visitor = VisitorDetails.objects.create(ip=ip, visited_count=1, last_visited=timezone.now())
    return dict(visitor=visitor)


def get_visitor_count(request):
    return dict(count=VisitorDetails.objects.all().count())
