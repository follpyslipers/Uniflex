from django.contrib.sitemaps import Sitemap
from .models import Location

class LocationSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Location.objects.all()

    def lastmod(self, obj):
        return obj.updated_at  # Assuming you have a field `updated_at` in your model
