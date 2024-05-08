from django.shortcuts import render
from  django.views.generic import TemplateView

# Create your views here.

class IngressoTemplateview(TemplateView):
    template_name = "pagina-compras"
