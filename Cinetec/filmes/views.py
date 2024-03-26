from django.shortcuts import render
from django.views.generic.list import ListView
from  django.views.generic import TemplateView,DetailView
from .models import listaFilmes

# Create your views here.



class indexListView(ListView):
        template_name = "index.html"
        queryset = listaFilmes.objects.all()
        context_object_name = 'filmes'


class sobreView(TemplateView):
    template_name = "sobre_nos.html"

class escolhidoDetailView(DetailView):
    model = listaFilmes    
    template_name = "escolhido.html"




