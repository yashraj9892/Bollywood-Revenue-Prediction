from django import forms
from django.contrib.auth.models import User
from django.contrib import auth
from predict.models import Movie


class Myform(forms.ModelForm):
    class Meta():
        model = Movie
        fields = '__all__'
