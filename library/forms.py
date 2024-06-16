from django import forms
from .models import E_Book,Course

class EBookUploadForm(forms.ModelForm):
    class Meta:
        model = E_Book
        fields = [ 'description', 'file']



    description = forms.CharField(
        label='Description',
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Enter description (optional)'})
    )


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_code', 'title')