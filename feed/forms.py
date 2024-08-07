from django import forms

from .models import Post


class PostCreationForm(forms.Form):
    topic = forms.CharField()
    text = forms.CharField(widget=forms.Textarea, max_length=1000)
