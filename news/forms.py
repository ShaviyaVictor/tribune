from django import forms
from django.contrib.auth.models import User




class NewsLetterForm(forms.Form) :
  username = forms.CharField(label='Your Name', max_length=30)
  email = forms.EmailField()

  