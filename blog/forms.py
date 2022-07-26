from django import forms
from django.forms import fields, widgets
from .models import Post, Comment

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='')
    class Meta:
        model = Comment
        fields = ['body',]



class UploadForm(forms.Form):  
    title = forms.CharField(label="Enter title",max_length=50) 
    file      = forms.FileField()
    content  = forms.CharField(label="content",max_length=900000)

    
  
  
class PostForm(forms.ModelForm): 
  
    class Meta: 
        model = Post 
        fields = ['title', 'image','author','content','date_posted','likes','saves'] 