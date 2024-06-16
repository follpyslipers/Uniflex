from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse
from user.models import User

def default_cover_image():
    return 'images/pdf.png'
# Constants for choices
APPROVED = 'Approved'
AWAITING_APPROVAL = 'Awaiting Approval'
DECLINED = 'Declined'

STATUS_CHOICES = [
    (APPROVED, 'Approved'),
    (AWAITING_APPROVAL, 'Awaiting Approval'),
    (DECLINED, 'Declined'),
]

# Custom function to define upload paths for user-related files
def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.user.id, ext)
    return 'user_{0}/{1}'.format(instance.user.id, filename)

# Model representing a faculty member
class Faculty(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='faculty/images')
    updated_at = models.DateTimeField(auto_now=True, blank=True , null=True)
    
    
 
    
    @property
    def image_url(self):
        return self.image.url if self.image else ''  # Return empty string if no image is set

    @property
    def num_departments(self):
        return self.departments.count()  # Use the related_name to count departments

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('library:faculty_list')

    class Meta:
        ordering = ['name']  # Order by name

# Model representing an academic department
class Department(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, related_name='departments', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="department/images")
    updated_at = models.DateTimeField(auto_now=True, blank=True , null=True)
    

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('library:department_list', args=[self.faculty.id])
    class Meta:
        ordering = ['name']  # Order by name

# Model representing an academic course
class Course(models.Model):
    course_code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=70, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, blank=True , null=True)
    


    def get_absolute_url(self):
        return reverse('library:course_list', args=[self.department.id])

    def __str__(self):
        return self.course_code

    class Meta:
        ordering = ['course_code']  # Order by course code


# Custom function to define upload paths for user-related files
def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.user.id, ext)
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class E_Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, blank=True, null=True)
    file = models.FileField(
        upload_to='ebook/books/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'epub', 'mobi', 'txt', 'ppt', 'pptx', 'doc', 'docx'])],
    )
    cover_image = models.ImageField(upload_to='ebooks/covers/', default=default_cover_image)
    updated_at = models.DateTimeField(auto_now=True) 
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=AWAITING_APPROVAL, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='ebooks')

    def _str_(self):
        return self.title

    def get_absolute_url(self):
        return reverse('library:ebook_list', args=[self.course.id]) 

    def save(self, *args, **kwargs):
        if not self.title:
            # Generate title based on course code
            if self.course:
                base_title = self.course.course_code
                existing_ebooks = E_Book.objects.filter(course=self.course).order_by('uploaded_at')
                next_version = "1.0"
                if existing_ebooks.exists():
                    last_title = existing_ebooks.last().title
                    if '.' in last_title:
                        # Extract the version number part
                        version_part = last_title.split()[-1]
                        main, sub = map(int, version_part.split('.'))
                        if sub < 9:
                            next_version = f"{main}.{sub + 1}"
                        else:
                            next_version = f"{main + 1}.0"
                self.title = f"{base_title} {next_version}"
            else:
                self.title = "Untitled"
        super().save(*args, **kwargs)


    @classmethod
    def search(cls, query):
        return cls.objects.filter(
            models.Q(title__icontains=query) |
            models.Q(description__icontains=query) |
            models.Q(course_course_code_icontains=query)
        ).distinct()

    class Meta:
        ordering = ['-uploaded_at']
