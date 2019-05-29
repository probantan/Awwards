from django import forms
from django.contrib.auth.models import User
from . models import Profile, Project
# from .models import Profile

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         list_display = []

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()       


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user', 'pub_date', 'profile', 'landing_image']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields= ['username', 'email']

        
class ProfileUpdateForm (forms.ModelForm):
    class Meta:
        model= Profile  
        fields=['profile_pic', 'bio']       