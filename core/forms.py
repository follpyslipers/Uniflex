# forms.py
from django import forms
from .models import EmailSubscription, FeedBack

class EmailSubscriptionForm(forms.ModelForm):
    class Meta:
        model = EmailSubscription
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Your email address'})
        }



class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ['feedback']
        widgets = {
            'feedback': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
        labels = {
            'feedback': 'Your Feedback',
        }