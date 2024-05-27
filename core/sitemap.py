from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return ['core:home', 'core:about', 'core:privacy', 'core:terms']

    def location(self, item):
        return reverse(item)


