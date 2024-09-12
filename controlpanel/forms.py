from django import forms
from home.models import Post

class CreateArticleForm(forms.ModelForm):
    """ Create a form based on the Post model """
    class Meta:
        model = Post
        fields = ['title', 'body', 'categories', 'cover_image']
        widgets = {
            'categories': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Enter the Article Title',
            'body': 'Enter the Article body text',
        }

        
        self.fields['title'].widget.attrs['autofocus'] = True

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control mb-3'
            self.fields[field].label = False