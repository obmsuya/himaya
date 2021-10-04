from django import forms
from home.models import Post
from home.models import Post4
from home.models import Friend




class HomeForm(forms.ModelForm):
    post= forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Put book link....'
        }
    ))
    class Meta:
        model = Post
        fields=('user','post', 'bookname')
        
class FriendForm(forms.ModelForm):
    
    class Meta:
        model = Friend
        fields=('users', 'current_user')        
        
        
class ClassRegistration(forms.ModelForm):
    fullname= forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Your first and last name....'
        }
    ))
    
    
   
    
    username= forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Your login name created previously....'
        }
    ))
    
    region= forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Your region or state ....'
        }
    ))
    

    class Meta:
        model = Post4
        fields = ('fullname', 'username','country', 'region','phone')

class PostForm2(forms.ModelForm):

    fullname= forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Weka hapa jina lako la kwanza na la mwisho....'
        }
    ))

    book= forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Weka hapa jina la kitabu unachokitaka kununu ....'
        }
    ))



    class Meta:
        model = Post4
        fields= [
            "fullname",
            "book",   
            
        ]
        
        
        
