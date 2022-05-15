
from dataclasses import fields
from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
    

class ShareForm(forms.Form):
    name = forms.CharField(max_length=25)
    body = forms.CharField(widget=forms.Textarea)
    to = forms.EmailField()

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'status']
