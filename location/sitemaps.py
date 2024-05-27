from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Location

class LocationSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Location.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('location:location_list') + f"?id={obj.id}"
