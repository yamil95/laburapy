from django.shortcuts import render
from django.views.generic.base import TemplateView

from django.urls import reverse_lazy
# Create your views here.

from applications.users.forms import SearchProfesionForm

class home(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchProfesionForm()  # Agrega el formulario al contexto
        return context
