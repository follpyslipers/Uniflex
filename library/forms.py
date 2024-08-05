from django import forms
from .models import E_Book,Course

class EBookUploadForm(forms.ModelForm):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=True)

    class Meta:
        model = E_Book
        fields = ['files']  # Note: We're using 'files' here to handle multiple uploads


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_code', 'title')
        
    
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Title Optional'})
    )
    course_code = forms.CharField(
        label='Course Code',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Course Code'})
    )