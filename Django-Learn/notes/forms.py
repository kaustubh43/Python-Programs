from django import forms
from django.core.exceptions import ValidationError

from .models import Note


class NotesForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'text', 'author', 'comments',)

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'django' not in title.lower():
            raise ValidationError('we only accept notes about Django')
        return title


