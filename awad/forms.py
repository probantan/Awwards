from django import forms
from django.contrib.auth.models import User
from . models import Profile
# from .models import Profile

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         list_display = []

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()       



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields= ['username', 'email']

        
class ProfileUpdateForm (forms.ModelForm):
    class Meta:
        model= Profile  
        fields=['profile_pic', 'bio']       