from django import forms


class CommentForm(forms.Form):
    text = forms.CharField(max_length=200, widget=forms.Textarea)
