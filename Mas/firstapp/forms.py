from django.contrib.auth.models import User
from .models import *
from django import forms
from django.contrib.auth.forms import  UserChangeForm, UserCreationForm


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    soglasie = forms.BooleanField(label='Согласие на обработку персональных данных', widget=forms.BooleanField)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Поля паролей не совпадают!')
        return cd['password2']

    def soglasie(self):
        cd = self.cleaned_data
        if cd['soglasie'] != True:
            raise forms.ValidationError('Поле согласие на обработку персональных данных, обязательно!')
            return cd
        return cd['soglasie']


class UserPageForm(forms.ModelForm):
    picture = forms.ImageField(label='Ваш аватар', widget=forms.ImageField)
    class Meta:
        model = Person
        last_name = User.last_name
        first_name = User.first_name
        fields = ('patronomyc', 'user')



