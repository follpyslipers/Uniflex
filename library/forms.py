from django import forms
from .models import E_Book, Course

class EBookUploadForm(forms.ModelForm):
    file = forms.FileField(widget=forms.ClearableFileInput(), required=True)

    class Meta:
        model = E_Book
        fields = ['file']

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
