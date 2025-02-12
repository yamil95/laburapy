from django.db.models.query import QuerySet
from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from applications.profesiones.models import Profesion

from django.views.generic import (
    View,
    CreateView,
    ListView
)

from django.views.generic.edit import (
    FormView
)

from .forms import (
    UserRegisterForm, 
    LoginForm,
    UpdatePasswordForm,
    SearchProfesionForm,
    VerificationForm
)
from .functions import code_generator
#
from .models import User
# 

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = "/"
    
    
    def form_valid(self, form):
        codigo = code_generator()
        usuario = User.objects.create_user(
                form.cleaned_data["email"],
                form.cleaned_data['password1'],
                genero=form.cleaned_data['genero'],
                full_name = form.cleaned_data['full_name'],
                codigo_registro = codigo,
                dni = form.cleaned_data["dni"],
                celular = form.cleaned_data["celular"]
            )

        usuario.save()  
        form.enviar_codigo(form.cleaned_data["celular"],codigo)
        return HttpResponseRedirect(
            reverse('users_app:user-verification',kwargs={"pk":usuario.id})
        )



class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:pagina-inicio')

    def form_valid(self, form):

        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class LogoutView(View):

    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )


class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'users/update.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users_app:user-login')
    login_url = reverse_lazy('users_app:user-login')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            email=usuario.email,
            password=form.cleaned_data['password1']
        )

        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()

        logout(self.request)
        return super(UpdatePasswordView, self).form_valid(form)



class VerificationCode (FormView):
    
    template_name='users/verification.html'
    form_class = VerificationForm
    success_url = reverse_lazy('users_app:user-login')
    
    
    def get_form_kwargs(self) :
        kwargs = super(VerificationCode,self).get_form_kwargs()
        kwargs.update ({"pk":self.kwargs["pk"]})
        return kwargs 
    
    def form_valid(self, form):
        User.objects.filter(id= self.kwargs["pk"]).update(is_active= True)
        return super(VerificationCode,self).form_valid(form)
    
    