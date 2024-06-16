from django import forms
from .models import E_Book,Course

class EBookUploadForm(forms.ModelForm):
    class Meta:
        model = E_Book
        fields = ['description', 'file']

    # title = forms.CharField(
    #     label='Title',
    #     widget=forms.TextInput(attrs={'placeholder': 'Enter title'})
    # )

    description = forms.CharField(
        label='Description',
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Enter description (optional)'})
    )



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