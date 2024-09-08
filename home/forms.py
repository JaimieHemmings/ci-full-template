
from django import forms
from .models import Message
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    """ Create a form based on the Message model """

    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(validators=[EmailValidator()], required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)