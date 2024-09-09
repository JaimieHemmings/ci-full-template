from django import forms
from .models import Portfolio

class PortfolioForm(forms.ModelForm):
  """ Create a form based on the Portfolio model """

  class Meta:
    model = Portfolio
    fields = ['title', 'description']

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    placeholders = {
      'title': 'Enter the title',
      'description': 'Enter the description',
    }

    for field in self.fields:
      placeholder = f'{placeholders[field]}'
      self.fields[field].widget.attrs['placeholder'] = placeholder
      self.fields[field].widget.attrs['class'] = 'form-control mb-3'
      self.fields[field].label = False