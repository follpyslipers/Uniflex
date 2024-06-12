from django import forms
from .models import E_Book

class EBookUploadForm(forms.ModelForm):
    class Meta:
        model = E_Book
        fields = ['title', 'description', 'file']

    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(attrs={'placeholder': 'Enter title'})
    )

    description = forms.CharField(
        label='Description',
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Enter description (optional)'})
    )

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 5 characters long")
        return title