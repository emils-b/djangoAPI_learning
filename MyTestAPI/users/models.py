from django.db import models
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# jāpārveido tagadējā reģistrēšanās un login sistēma, lai ir vairāk custom

class registerForm(UserCreationForm):
    #id = models.IntegerField(null=False, primary_key=True)
    first_name = forms.CharField()
    last_name = forms.CharField()
    #image = forms.ImageField(upload_to='media', default='def.png')
    image = forms.ImageField(required=False) #jaatrod kā uzlikt defoultu attēli
    #consent = forms.BooleanField(default=False)
    consent = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'consent']


