from django import forms
from home.models import Post

class CreateArticleForm(forms.ModelForm):
    """ 
    Form for creating or updating an article based on the Post model.
    """

    class Meta:
        model = Post
        fields = ['title', 'body', 'categories', 'cover_image']
        widgets = {
            'categories': forms.CheckboxSelectMultiple(),  # Use checkboxes for categories
        }

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with custom settings for fields.
        """
        super().__init__(*args, **kwargs)
        
        # Placeholder text for form fields
        placeholders = {
            'title': 'Enter the Article Title',
            'body': 'Enter the Article body text',
        }

        # Set autofocus on the title field
        self.fields['title'].widget.attrs['autofocus'] = True
        
        # Custom label for categories field
        self.fields['categories'].label = 'Categories*'
        
        # Iterate through all fields to apply custom settings
        for field in self.fields:
            if field != 'categories':
                # Add CSS classes to fields for styling
                self.fields[field].widget.attrs['class'] = 'form form-control mb-3'
                
                if field != 'cover_image':
                    # Set placeholder text, indicating required fields with an asterisk
                    if self.fields[field].required:
                        placeholder = f'{placeholders[field]} *'
                    else:
                        placeholder = placeholders[field]
                    
                    self.fields[field].widget.attrs['placeholder'] = placeholder
                    
                    # Hide the label for these fields
                    self.fields[field].label = False