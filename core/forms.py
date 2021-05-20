from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core import validators
from .models import PortfolioUpdate


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_count = User.objects.filter(email=email).count()

        if email_count>0:
            raise forms.ValidationError('Email already exists.')
 
        return email

class PortfolioUpdateForm(forms.ModelForm):
    class Meta:
        model = PortfolioUpdate
        fields = '__all__'
        # fields = ('name', 'title', 'about', 'phone', 'email','city','country','facebook','github','uni','uni_subject','uni_result','uni_passing','clg','clg_group','clg_result','clg_passing','skills','company','designation','period','theme','image')
        exclude=['user','skills','theme']                  
     
     
    
     
    

