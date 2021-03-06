from django import forms
from django.contrib.auth.models import User
from .models import NewsletterRecipients




class NewsLetterForm(forms.ModelForm) :
  # username = forms.CharField(label='Your Name', max_length=30)
  email = forms.EmailField()

  class Meta :
    model = NewsletterRecipients
    fields = [
      'username',
      'email',      
    ]

  