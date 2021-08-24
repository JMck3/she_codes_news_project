from django import forms
from django.forms import ModelForm
from .models import NewsStory

# allow Django to infer all the form fields and validation from a model
class StoryForm(ModelForm):
    class Meta: 
        model = NewsStory
        fields = [''] # anything from form field
        fields = ['title', 'pub_date', 'content', 'img_url']
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'),
        attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
