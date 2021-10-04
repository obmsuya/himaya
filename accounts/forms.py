from django import forms
from . import models
# from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm, UserChangeForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','password')


class UserProfileForm(forms.ModelForm):
    Proffession= forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Put activation code here....'
        }
    ))
    
    upliner= forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Put upliner name here....'
        }
    ))
    
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Put new member name....'
        }
    ))
    
    class Meta:
        # s
        fields=('user','Proffession','name','upliner', 'Maelezo', 'phone', 'image')