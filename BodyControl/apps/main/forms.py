from django import forms
from django.core.exceptions import ValidationError
from .models import DatosUser
from django.forms.widgets import Textarea
from django.contrib.auth.models import User




#VALIDADORES-------------------------------------------------------------------
def check_size(value):
    if len(value) < 5 or len(value) > 30:
        raise ValidationError("Title shouldn't have less than 5 and more than 30 chars")
    
def check_pass(value):
    if len(value) < 2:
        raise ValidationError("La password debe tener una combinacion de Letras y numeros")
    
 
def check_user(value):
    if len(value) < 5:
        raise ValidationError("El usuario debe contener mas de 4 caracteres")
    return value

def check(value):
    if len(value) < 5:
        raise ValidationError("Debe contener mas de 4 caracteres")
    return value
    
  
 
BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
#--------------------------------------FORMULARIOS------------------------------------------


##---------------PARA INICIAR A USAR BODY CONTROL
SEX = (('F', 'Feminino'),
                            ('M', 'Masculino'),
                            )

class BodyStart(forms.ModelForm):
    #u = DatosUser.objects.get( user = user)
    sexo = forms.MultipleChoiceField(required=False,
        widget=forms.SelectMultiple, choices=SEX)
    class Meta: 
        model = DatosUser
        exclude = ['user']

#----------------PARA REGISTRARME EN BODY CONTROL
class FormRegister(forms.ModelForm):
    password1 = forms.CharField(label="Password",
        widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    password2 = forms.CharField(label="Confirm Password",
       widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')
        widgets = { 
           'username':forms.TextInput(attrs={'class': 'form-control'}),
           'first_name':forms.TextInput(attrs={'class': 'form-control'}),
           'last_name':forms.TextInput(attrs={'class': 'form-control'}),
           'email':forms.TextInput(attrs={'class': 'form-control'}),

        }
