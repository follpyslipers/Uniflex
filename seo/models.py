from django.db import models
from django_seo_js.models import Seo

class MySeoModel(Seo):
    title = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.CharField(max_length=255)

    class Meta:
        verbose_name = "SEO Configuration"
        verbose_name_plural = "SEO Configurations"

    def __str__(self):
        return self.title
