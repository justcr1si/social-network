from django import forms


class PostProcessingForm(forms.Form):
    topic = forms.CharField()
    text = forms.CharField(widget=forms.Textarea, max_length=1000)
