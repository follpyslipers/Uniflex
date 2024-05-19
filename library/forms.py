from django import forms
from .models import E_Book

class EBookForm(forms.ModelForm):
    class Meta:
        model = E_Book
        fields = ['title', 'description', 'course', 'file']
