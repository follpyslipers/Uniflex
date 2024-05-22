from django.db import models
from django.contrib.auth.models import AbstractUser

def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.user.id, ext)
    return 'user_{0}/{1}'.format(instance.user.id,  filename)

class User(AbstractUser):
    matric_number = models.CharField(max_length=100 , unique=True) 
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_class_rep = models.BooleanField(default=False)

    USERNAME_FIELD = 'matric_number'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    department = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name