from dataclasses import fields
from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'note')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'note': forms.Textarea(attrs={'class': 'form-control mb-5'})
        }
        labels = {
            'text': 'Write Your Thoughts Here'
        }


    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise forms.ValidationError('We only accept topics about Django!')
        return title