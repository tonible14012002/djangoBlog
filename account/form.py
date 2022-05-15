
from django import forms
from django.forms import ModelForm, Form
from django.contrib.auth.models import User
from .models import Profile
from blogSite.models import Post

class RegistrationForm(ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email'] 
    
    def clean_first_name(self):
        firstname = self.cleaned_data['first_name']
        if not firstname:
            raise forms.ValidationError('Enter your first name')
        return firstname

    def clean_last_name(self):
        lastname = self.cleaned_data['last_name']
        if not lastname:
            raise forms.ValidationError('Enter your last name')
        return lastname

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Password don\'t match')
        return data['password2']
    def clean_email(self):
        data = self.cleaned_data
        if User.objects.filter(email=data['email']).\
            exclude(username=data['username']).exists():
            raise forms.ValidationError('email have already be used by another account')
        return data['email']

class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = [ 'avatar', 'date_of_birth',]

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'status']
