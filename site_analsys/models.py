from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=256)
    visit_date = models.DateField(default=timezone.now)
    page_visited = models.CharField(max_length=256)
    visit_time = models.DateTimeField(auto_now_add=True)
    session_key = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.ip_address} visited on {self.visit_date}"
