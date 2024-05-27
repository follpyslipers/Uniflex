from django.contrib.sitemaps import Sitemap
from .models import Faculty, Department, Course, E_Book

class FacultySitemap(Sitemap):
    def items(self):
        return Faculty.objects.all()
    def location(self, item):
        return item.get_absolute_url()

class DepartmentSitemap(Sitemap):
    def items(self):
        return Department.objects.all()
    def location(self, item):
        return item.get_absolute_url()

class CourseSitemap(Sitemap):
    def items(self):
        return Course.objects.all()
    def location(self, item):
        return item.get_absolute_url()

class EBookSitemap(Sitemap):
    def items(self):
        return E_Book.objects.all()
    def location(self, item):
        return item.get_absolute_url()

# Then in your main urls.py
