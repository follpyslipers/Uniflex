from django import forms
from .models import E_Book

class EBookUploadForm(forms.ModelForm):
    class Meta:
        model = E_Book
        fields = ['title', 'description', 'file', 'cover_image']
