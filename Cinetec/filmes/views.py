from typing import Any
from django.shortcuts import render
from django.views.generic.list import ListView
from  django.views.generic import TemplateView,DetailView
from .models import listaFilmes
from django.contrib.auth import user_logged_in

# Create your views here.


class indexListView(ListView):
        template_name = "index.html"
        queryset = listaFilmes.objects.all()
        context_object_name = 'filmes'

class programacaoListView(ListView):
    template_name = "programacao.html"
    queryset = listaFilmes.objects.all()
    context_object_name = 'filmes'
    


class sobreView(TemplateView):
    template_name = "sobre_nos.html"

class escolhidoDetailView(DetailView):
    model = listaFilmes    
    template_name = "escolhido.html"




