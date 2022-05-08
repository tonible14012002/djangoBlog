
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
    

class ShareForm(forms.Form):
    name = forms.CharField(max_length=25)
    body = forms.CharField(widget=forms.Textarea)
    to = forms.EmailField()
