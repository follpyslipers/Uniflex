from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class NickName(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=255)
    google_link = models.URLField(max_length=900)
    nick_name = models.OneToOneField(NickName, on_delete=models.CASCADE ,blank=True , null=True)
    categories = models.ManyToManyField(Category)
    def __str__(self):
        return self.name
    
    @classmethod
    def search(cls, query):
        return cls.objects.filter(
            models.Q(name__icontains=query) | 
            models.Q(nick_name__name__icontains=query) |
            models.Q(categories__name__icontains=query)
        ).distinct()
