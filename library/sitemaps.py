from django.contrib.sitemaps import Sitemap
from .models import Faculty, Department, Course, E_Book

class FacultySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Faculty.objects.all()

    def lastmod(self, obj):
        return obj.updated_at  # Assuming you have a field `updated_at` in your model

class DepartmentSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Department.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

class CourseSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Course.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

class EBookSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return E_Book.objects.all()

    def lastmod(self, obj):
        return obj.uploaded_at
