from django import forms
from home.models import Post
from home.models import Post4
from home.models import Downliner




class HomeForm(forms.ModelForm):
    post= forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'write a post....'
        }
    ))
    class Meta:
        model = Post
        fields=('post',)
        
        
        
        
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
        
        
        
class Images(forms.ModelForm):
    class Meta:
        model = Downliner 
        fields= [
            "title",
            "content",
            "image",
            
        ]