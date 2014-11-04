from django import forms
from django.core.exceptions import ValidationError
from .models import *
from django.forms.widgets import Textarea
from django.contrib.auth.models import User



class Estado(forms.ModelForm):
    class Meta: 
        model = Estado
