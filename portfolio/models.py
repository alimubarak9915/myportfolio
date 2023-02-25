from django.db import models


class VisitorDetails(models.Model):
    ip = models.CharField(max_length=20, blank=True, null=True)
    last_visited = models.DateTimeField(null=True, blank=True)
    visited_count = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Visitor Details'

    def __str__(self):
        return self.ip
