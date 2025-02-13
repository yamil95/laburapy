from django import forms
from django.contrib.auth import authenticate
#
from applications.profesiones.models import Profesion
from .models import User
from applications.profesiones.models import Profesion

from celery.result import AsyncResult
from applications.ubicaciones.models import (
    Provincias,
    
)
 
from applications.users.tasks import   tarea_celery

def choices_provincia ():
    provincias = Provincias.objects.all()
    choices = [(provincia.id,provincia.nombre) for provincia in provincias]
    return choices

def choices_profesiones ():
    profesiones = Profesion.objects.all()
    choices = [(profesion.id,profesion.name) for profesion in profesiones]
    return choices




class UserRegisterForm(forms.ModelForm):
    

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña'
            }
        )
    )


    date_birth = forms.DateField(
        label='Fecha de nacimiento',
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Fecha de nacimiento'
            }
        )
    ) 
    def enviar_codigo(self,celular,codigo):
        
        resultado = tarea_celery.delay(celular,codigo)
        

    
    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = (
            'email',
            'full_name',
            "dni",
            "genero",
            "celular"
        )

    
    
    def clean(self):
        cleaned_data = super(UserRegisterForm,self).clean()
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')
        return cleaned_data

class LoginForm(forms.Form):
    email = forms.CharField(
        label='E-mail',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Correo Electronico',
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')
        
        return cleaned_data



class UpdatePasswordForm(forms.Form):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Actual'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Nueva'
            }
        )
    )

def choices_profesiones ():
    profesiones = Profesion.objects.all()
    choices = [(profesion.id,profesion.name)for profesion in profesiones]
    return choices

class SearchProfesionForm(forms.ModelForm):
    


    provincia = forms.ChoiceField(choices=choices_provincia, required=False)
    localidad = forms.ChoiceField(choices= [], required=False)
    profesiones = forms.ChoiceField (choices=choices_profesiones,required=True)


    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = (
            'genero',
            'provincia',
            'localidad'
        )
        
class VerificationForm(forms.Form):
    
    codigo = forms.CharField(max_length=6,required=True)    

    def __init__(self, pk, *args, **kwargs):
        self.id_user = pk
        super(VerificationForm, self).__init__(*args, **kwargs)
    
    
    def clean_codigo(self):
        
        codigo = self.cleaned_data["codigo"]
        
        if len(codigo) == 6:
            activo = User.objects.validar_codigo(
                self.id_user,
                codigo
            )
            
            if not activo:
                raise forms.ValidationError("el codigo es incorrecto")

        else:
            raise forms.ValidationError("el codigo es incorrecto")