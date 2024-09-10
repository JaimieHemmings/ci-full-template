from django import forms
from .models import ProjectMessage

class ProjectFeedbackForm(forms.ModelForm):
    """ Create a form based on the ProjectMessage model """
    class Meta:
        model = ProjectMessage
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Enter your name',
            'message': 'Enter your message',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control mb-3'
            self.fields[field].label = False