from django import forms
from .models import BlogInfo,Cate,Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BlogPostForms(forms.ModelForm):
    class Meta:
        model = BlogInfo
        fields =('title','b_cat','b_img','body',)

class PostEditForm(forms.ModelForm):
    class Meta:
        model = BlogInfo
        fields =('title','b_cat','b_img','body',)
    
class CategoryPostForms(forms.ModelForm):
    class Meta:
        model = Cate
        fields =('c_name','c_img','c_status')

class CateEditForms(forms.ModelForm):
    class Meta:
        model = Cate
        fields =('c_name','c_img','c_status')

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,)
    last_name = forms.CharField(max_length=30,)
    email = forms.EmailField(max_length=30,)
    dob =forms.DateField(help_text="Required Formate: YYYY-MM-DD")
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','dob')
    

