from django import forms
from django.contrib.auth.models import User
from . models import Profile, Project,Rate
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
        exclude = ['user', 'pub_date', 'profile']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields= ['username', 'email']

        
class ProfileUpdateForm (forms.ModelForm):
    class Meta:
        model= Profile  
        fields=['profile_pic', 'bio']       

class RateForm(forms.ModelForm):
    class Meta:
        model =Rate
        exclude= ['user','project']       