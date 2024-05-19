from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=100)
    location_lat = models.FloatField()
    location_long = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name
