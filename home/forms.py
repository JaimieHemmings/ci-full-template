
from django import forms
from .models import Message

class ContactForm(forms.ModelForm):
    """ Create a form based on the Message model """
    class Meta:
        model = Message
        fields = ['interest','name', 'email', 'message']
        widgets = {
            'interest': forms.Select(choices=Message.INTEREST_CHOICES),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'interest': 'Select your interest',
            'name': 'Enter your name',
            'email': 'Enter your email address',
            'message': 'Enter your message',
        }

        self.fields['email'].widget.input_type = 'email'
        self.fields['interest'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control mb-3'
            self.fields[field].label = False