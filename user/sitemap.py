from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class UserSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5  # Adjust priority as needed

    def items(self):
        return ['user:sign-in', 'user:sign-up', 'user:sign-out']

    def location(self, item):
        return reverse(item)
