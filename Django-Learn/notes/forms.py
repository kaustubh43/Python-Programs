from django import forms
from django.core.exceptions import ValidationError

from .models import Note


class NotesForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'text', 'author', 'comments',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control my-5'}),
            'comments': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'author': forms.TextInput(attrs={'class': 'form-control my-5'})
        }
        labels = {
            'text': 'Write your thoughts here',
            'title': 'Title',
            'author': 'Author',
            'comments': 'Comments',
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'django' not in title.lower():
            raise ValidationError('we only accept notes about Django')
        return title


