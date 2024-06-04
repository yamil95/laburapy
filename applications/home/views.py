from django.shortcuts import render
from django.views.generic.base import TemplateView

from django.urls import reverse_lazy
# Create your views here.



class home(TemplateView):
    template_name = "index.html"
    success_url = reverse_lazy('.')
